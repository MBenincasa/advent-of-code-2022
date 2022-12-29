"""
--- Part Two ---

As you walk up the hill, you suspect that the Elves will want to turn this into a hiking trail. The beginning isn't very scenic, though; perhaps you can find a better starting point.
To maximize exercise while hiking, the trail should start as low as possible: elevation a. The goal is still the square marked E. However, the trail should still be direct, taking the fewest steps to reach its goal. So, you'll need to find the shortest path from any square at elevation a to the square marked E.

Again consider the example from above:

Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi

Now, there are six choices for starting position (five marked a, plus the square marked S that counts as being at elevation a). If you start at the bottom-left square, you can reach the goal most quickly:

...v<<<<
...vv<<^
...v>E^^
.>v>>>^^
>^>>>>>^

This path reaches the goal in only 29 steps, the fewest possible.
What is the fewest steps required to move starting from any square with elevation a to the location that should get the best signal?

"""

from collections import deque
from typing import Deque

def bfs(
    graph: dict[tuple[int, int], set[tuple[int, int]]],
    start: tuple[int, int],
    end: tuple[int, int],
):
    visited = {start: 0}
    steps = 0
    queue: Deque[tuple[tuple[int, int], int]] = deque()
    queue.append((start, steps))
    while queue:
        current, steps = queue.popleft()
        if current == end:
            return steps
        for neighbour in graph[current]:
            if neighbour not in visited:
                visited[neighbour] = steps + 1
                queue.append((neighbour, steps + 1))
    return -1

def get_elevation(elevation: str) -> int:
    if elevation == "S":
        return get_elevation("a")
    elif elevation == "E":
        return get_elevation("z")
    return ord(elevation) - ord("a")

def construct_graph(lines: list[str]) -> dict[tuple[int, int], set[tuple[int, int]]]:
    graph = {}
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            coord = (x, y)
            children = set()
            candidates = [
                (x + dx, y + dy)
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]
                if 0 <= x + dx < len(line) and 0 <= y + dy < len(lines)
            ]
            for x1, y1 in candidates:
                if get_elevation(lines[y1][x1]) - get_elevation(char) <= 1:
                    children.add((x1, y1))
            graph[coord] = children
    return graph

def get_start_and_end_point(lines):
    for i, line in enumerate(lines):
        if line.find("S") != -1:
            start = (line.find("S"), i)
        if line.find("E") != -1:
            end = (line.find("E"), i)
    return start, end

def main() -> None:
    with open('../input.txt', 'r') as file_input:
        lines = [line.strip() for line in file_input.readlines()]
        start, end = get_start_and_end_point(lines)
        print(f"start: {start} end: {end}")
        graph = construct_graph(lines)
        #print(f"graph: {graph}")
        
        start_candidates = {(x, y) for x, y in graph if get_elevation(lines[y][x]) == 0}
        steps_required = []
        for start in start_candidates:
            steps = bfs(graph, start, end)
            if steps != -1:
                steps_required.append(steps)

        print(f"The fewest steps required is: {min(steps_required)}")

if __name__ == "__main__":
    main()