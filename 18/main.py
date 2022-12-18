import sys

sys.setrecursionlimit(1000000)

with open("input.txt") as f:
    input = f.readlines()
input = [line.strip().split(",") for line in input]
cubes = set([tuple(int(coord) for coord in line) for line in input])


def count_surface(cubes):
    surface = 0
    for cube in cubes:
        sides = [
            (cube[0] - 1, cube[1], cube[2]),
            (cube[0] + 1, cube[1], cube[2]),
            (cube[0], cube[1] - 1, cube[2]),
            (cube[0], cube[1] + 1, cube[2]),
            (cube[0], cube[1], cube[2] - 1),
            (cube[0], cube[1], cube[2] + 1),
        ]
        for side in sides:
            surface += 1 if side not in cubes else 0
    return surface


print(count_surface(cubes))

xs = [cube[0] for cube in cubes]
ys = [cube[1] for cube in cubes]
zs = [cube[2] for cube in cubes]
minx, maxx, miny, maxy, minz, maxz = (
    min(xs),
    max(xs),
    min(ys),
    max(ys),
    min(zs),
    max(zs),
)
bounding_box = ((minx - 1, miny - 1, minz - 1), (maxx + 1, maxy + 1, maxz + 1))
bounding_box_len = (
    bounding_box[1][0] - bounding_box[0][0] + 1,
    bounding_box[1][1] - bounding_box[0][1] + 1,
    bounding_box[1][2] - bounding_box[0][2] + 1,
)
bounding_box_surface = (
    2 * bounding_box_len[0] * bounding_box_len[1]
    + 2 * bounding_box_len[0] * bounding_box_len[2]
    + 2 * bounding_box_len[1] * bounding_box_len[2]
)


def is_in_boundary(cube):
    return (
        bounding_box[0][0] <= cube[0] <= bounding_box[1][0]
        and bounding_box[0][1] <= cube[1] <= bounding_box[1][1]
        and bounding_box[0][2] <= cube[2] <= bounding_box[1][2]
    )


filled = set()


def flood_fill(cube):
    if cube in filled or not is_in_boundary(cube):
        return
    filled.add(cube)
    sides = [
        (cube[0] - 1, cube[1], cube[2]),
        (cube[0] + 1, cube[1], cube[2]),
        (cube[0], cube[1] - 1, cube[2]),
        (cube[0], cube[1] + 1, cube[2]),
        (cube[0], cube[1], cube[2] - 1),
        (cube[0], cube[1], cube[2] + 1),
    ]
    for side in sides:
        if side not in cubes:
            flood_fill(side)


flood_fill(bounding_box[0])
print(count_surface(filled) - bounding_box_surface)
