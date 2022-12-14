from enum import Enum

with open("input.txt") as f:
    input = f.readlines()
input = [line.strip() for line in input]

paths = []
for line in input:
    points = line.split(" -> ")
    path = []
    for point in points:
        point = point.split(",")
        path.append((int(point[0]), int(point[1])))
    paths.append(path)

sand_start = (500, 0)

points_y = []
for path in paths:
    points_y.extend([point[1] for point in path])
abyss_y = max(points_y) + 1


class TileType(Enum):
    AIR = 0
    ROCK = 1
    SAND = 2


original_cave = {}
for path in paths:
    for i in range(len(path) - 1):
        start = path[i]
        end = path[i + 1]
        if start[0] == end[0]:
            diff = end[1] - start[1]
            if diff > 0:
                for j in range(diff + 1):
                    original_cave[(start[0], start[1] + j)] = TileType.ROCK
            else:
                for j in range(0, diff - 1, -1):
                    original_cave[(start[0], start[1] + j)] = TileType.ROCK
        else:
            diff = end[0] - start[0]
            if diff > 0:
                for j in range(diff + 1):
                    original_cave[(start[0] + j, start[1])] = TileType.ROCK
            else:
                for j in range(0, diff - 1, -1):
                    original_cave[(start[0] + j, start[1])] = TileType.ROCK


def is_air(cave, next_point):
    return next_point not in cave or cave[next_point] == TileType.AIR


def simulate_sand(cave, units_of_sand, prev_point):
    while True and prev_point[1] < abyss_y:
        next_point = (prev_point[0], prev_point[1] + 1)
        if is_air(cave, next_point):
            prev_point = next_point
        else:
            next_point = (prev_point[0] - 1, prev_point[1] + 1)
            if is_air(cave, next_point):
                prev_point = next_point
            else:
                next_point = (prev_point[0] + 1, prev_point[1] + 1)
                if is_air(cave, next_point):
                    prev_point = next_point
                else:
                    cave[prev_point] = TileType.SAND
                    units_of_sand += 1
                    break
    return prev_point, units_of_sand


cave = original_cave.copy()
units_of_sand = 0
while True:
    prev_point = sand_start
    prev_point, units_of_sand = simulate_sand(cave, units_of_sand, prev_point)
    if prev_point[1] >= abyss_y:
        break
print(units_of_sand)

cave = original_cave.copy()
units_of_sand = 0
while True:
    prev_point = sand_start
    prev_point, units_of_sand = simulate_sand(cave, units_of_sand, prev_point)
    if prev_point[1] >= abyss_y:
        cave[prev_point] = TileType.SAND
        units_of_sand += 1
    if prev_point == sand_start:
        break
print(units_of_sand)
