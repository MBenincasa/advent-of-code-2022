"""
--- Part Two ---

You realize you misread the scan. There isn't an endless void at the bottom of the scan - there's floor, and you're standing on it!
You don't have time to scan the floor, so assume the floor is an infinite horizontal line with a y coordinate equal to two plus the highest y coordinate of any point in your scan.

In the example above, the highest y coordinate of any point is 9, and so the floor is at y=11. (This is as if your scan contained one extra rock path like -infinity,11 -> infinity,11.) With the added floor, the example above now looks like this:

        ...........+........
        ....................
        ....................
        ....................
        .........#...##.....
        .........#...#......
        .......###...#......
        .............#......
        .............#......
        .....#########......
        ....................
<-- etc #################### etc -->

To find somewhere safe to stand, you'll need to simulate falling sand until a unit of sand comes to rest at 500,0, blocking the source entirely and stopping the flow of sand into the cave. In the example above, the situation finally looks like this after 93 units of sand come to rest:

............o............
...........ooo...........
..........ooooo..........
.........ooooooo.........
........oo#ooo##o........
.......ooo#ooo#ooo.......
......oo###ooo#oooo......
.....oooo.oooo#ooooo.....
....oooooooooo#oooooo....
...ooo#########ooooooo...
..ooooo.......ooooooooo..
#########################

Using your scan, simulate the falling sand until the source of the sand becomes blocked. How many units of sand come to rest?

"""

def main() -> None:
    with open('../input.txt', 'r') as file_input:

        lines = [line.strip() for line in file_input.readlines()]
        blocks = set()

        for line in lines:
            points = [tuple(map(int, point.split(","))) for point in line.split(" -> ")]

            for i in range(len(points) - 1):
                point_start, point_end = points[i], points[i + 1]
                
                sx, sy = point_start
                ex, ey = point_end

                if sx == ex:
                    for y in range(min(sy, ey), max(sy, ey) + 1):
                        blocks.add((sx, y))
                else:
                    for x in range(min(sx, ex), max(sx, ex) + 1):
                        blocks.add((x, sy))

        max_y = max(py for px, py in blocks)
        for x in range(-1000, 1000):
            blocks.add((x, max_y + 2))

        steps = 0
        while True:
            steps += 1
            sand = (500, 0)

            for _ in range(1000):
                for dx, dy in [(0, 1), (-1, 1), (1, 1)]:
                    sx, sy = sand
                    next_point = (sx + dx, sy + dy)
                    if next_point not in blocks:
                        sand = next_point
                        break
                else:
                    break

            if sx == 500 and sy == 0:
                print(f"The sand units that stop are: {steps}")
                break

            blocks.add(sand)

if __name__ == "__main__":
    main()