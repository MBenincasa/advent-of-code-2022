"""
--- Day 12: Hill Climbing Algorithm ---

You try contacting the Elves using your handheld device, but the river you're following must be too low to get a decent signal.
You ask the device for a heightmap of the surrounding area (your puzzle input). The heightmap shows the local area from above broken into a grid; the elevation of each square of the grid is given by a single lowercase letter, where a is the lowest elevation, b is the next-lowest, and so on up to the highest elevation, z.
Also included on the heightmap are marks for your current position (S) and the location that should get the best signal (E). Your current position (S) has elevation a, and the location that should get the best signal (E) has elevation z.
You'd like to reach E, but to save energy, you should do it in as few steps as possible. During each step, you can move exactly one square up, down, left, or right. To avoid needing to get out your climbing gear, the elevation of the destination square can be at most one higher than the elevation of your current square; that is, if your current elevation is m, you could step to elevation n, but not to elevation o. (This also means that the elevation of the destination square can be much lower than the elevation of your current square.)

For example:

Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi

Here, you start in the top-left corner; your goal is near the middle. You could start by moving down or right, but eventually you'll need to head toward the e at the bottom. From there, you can spiral around to the goal:

v..v<<<<
>v.vv<<^
.>vv>E^^
..v>>>^^
..>>>>>^

In the above diagram, the symbols indicate whether the path exits each square moving up (^), down (v), left (<), or right (>). The location that should get the best signal is still E, and . marks unvisited squares.
This path reaches the goal in 31 steps, the fewest possible.
What is the fewest steps required to move from your current position to the location that should get the best signal?

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
        print(f"The fewest steps required is: {bfs(graph, start, end)}")

if __name__ == "__main__":
    main()