import re

input = [
    "        ...#    \n",
    "        .#..    \n",
    "        #...    \n",
    "        ....    \n",
    "...#.......#    \n",
    "........#...    \n",
    "..#....#....    \n",
    "..........#.    \n",
    "        ...#....\n",
    "        .....#..\n",
    "        .#......\n",
    "        ......#.\n",
    "\n",
    "10R5L5R10L4R5L5\n",
]
with open("input.txt") as f:
    input = f.readlines()
input = [line[:-1] for line in input]

map = input[:-2]
path = input[-1]

steps = re.split("[LR]", path)
orientations = re.split("\d+", path)[1:-1]
path = [int(steps[0])]
for orientation, step in zip(orientations, steps[1:]):
    path.extend([orientation, int(step)])

map_rows = [list(line) for line in map]
map_columns = list(zip(*map_rows))

orientation_map = {
    ("R", "L"): "U",
    ("R", "R"): "D",
    ("L", "L"): "D",
    ("L", "R"): "U",
    ("U", "L"): "L",
    ("U", "R"): "R",
    ("D", "L"): "R",
    ("D", "R"): "L",
}
orientation_value_map = {
    "L": 2,
    "R": 0,
    "U": 3,
    "D": 1,
}

start_position_y = 0
for i, v in enumerate(map_rows[0]):
    if v == ".":
        start_position_y = i
        break
start_position = (0, i)
start_orientation = "R"

orientation = start_orientation
position = start_position
for c in path:
    if isinstance(c, int):
        match orientation:
            case "L":
                row = map_rows[position[0]]
                row_len = len(row)
                while c > 0:
                    c -= 1
                    new_position_y = position[1] - 1
                    if new_position_y == -1:
                        # TODO find method??
                        looped_position_y = position[1]
                        while (
                            looped_position_y < row_len
                            and row[looped_position_y] != " "
                        ):
                            looped_position_y += 1
                        looped_position_y -= 1
                        if row[looped_position_y] == "#":
                            break
                        position = (position[0], looped_position_y)
                        continue
                    match row[new_position_y]:
                        case ".":
                            position = (position[0], new_position_y)
                        case "#":
                            break
                        case " ":
                            # TODO find method??
                            looped_position_y = position[1]
                            while (
                                looped_position_y < row_len
                                and row[looped_position_y] != " "
                            ):
                                looped_position_y += 1
                            looped_position_y -= 1
                            if row[looped_position_y] == "#":
                                break
                            position = (position[0], looped_position_y)
            case "R":
                row = map_rows[position[0]]
                row_len = len(row)
                while c > 0:
                    c -= 1
                    new_position_y = position[1] + 1
                    if new_position_y == row_len:
                        # TODO find method??
                        looped_position_y = position[1]
                        while looped_position_y >= 0 and row[looped_position_y] != " ":
                            looped_position_y = looped_position_y - 1
                        looped_position_y += 1
                        if row[looped_position_y] == "#":
                            break
                        position = (position[0], looped_position_y)
                        continue
                    match row[new_position_y]:
                        case ".":
                            position = (position[0], new_position_y)
                        case "#":
                            break
                        case " ":
                            # TODO find method??
                            looped_position_y = position[1]
                            while (
                                looped_position_y >= 0 and row[looped_position_y] != " "
                            ):
                                looped_position_y -= 1
                            looped_position_y += 1
                            if row[looped_position_y] == "#":
                                break
                            position = (position[0], looped_position_y)
            case "U":
                column = map_columns[position[1]]
                column_len = len(column)
                while c > 0:
                    c -= 1
                    new_position_x = position[0] - 1
                    if new_position_x == -1:
                        # TODO find method??
                        looped_position_x = position[0]
                        while (
                            looped_position_x < column_len
                            and column[looped_position_x] != " "
                        ):
                            looped_position_x += 1
                        looped_position_x -= 1
                        if column[looped_position_x] == "#":
                            break
                        position = (looped_position_x, position[1])
                        continue
                    match column[new_position_x]:
                        case ".":
                            position = (new_position_x, position[1])
                        case "#":
                            break
                        case " ":
                            # TODO find method??
                            looped_position_x = position[0]
                            while (
                                looped_position_x < column_len
                                and column[looped_position_x] != " "
                            ):
                                looped_position_x += 1
                            looped_position_x -= 1
                            if column[looped_position_x] == "#":
                                break
                            position = (looped_position_x, position[1])
            case "D":
                column = map_columns[position[1]]
                column_len = len(column)
                while c > 0:
                    c -= 1
                    new_position_x = position[0] + 1
                    if new_position_x == column_len:
                        # TODO find method??
                        looped_position_x = position[0]
                        while (
                            looped_position_x >= 0 and column[looped_position_x] != " "
                        ):
                            looped_position_x -= 1
                        looped_position_x += 1
                        if column[looped_position_x] == "#":
                            break
                        position = (looped_position_x, position[1])
                        continue
                    match column[new_position_x]:
                        case ".":
                            position = (new_position_x, position[1])
                        case "#":
                            break
                        case " ":
                            # TODO find method??
                            looped_position_x = position[0]
                            while (
                                looped_position_x >= 0
                                and column[looped_position_x] != " "
                            ):
                                looped_position_x -= 1
                            looped_position_x += 1
                            if column[looped_position_x] == "#":
                                break
                            position = (looped_position_x, position[1])
    else:
        orientation = orientation_map[(orientation, c)]
position = (position[0] + 1, position[1] + 1)
print(1000 * position[0] + 4 * position[1] + orientation_value_map[orientation])

face_size = len(map[0]) // 4


def get_looped_coordinates(coordinates, orientation):
    match orientation:
        case "L":
            x = coordinates[0]
            if x < face_size:
                return (face_size, 2 * face_size - (face_size - position[0])), "D"
            if x < 2 * face_size:
                return (
                    3 * face_size - 1,
                    3 * face_size + (2 * face_size - position[0] - 1),
                ), "U"
            return (
                2 * face_size - 1,
                2 * face_size - (position[0] - 2 * face_size) - 1,
            ), "U"
        case "R":
            x = coordinates[0]
            if x < face_size:
                return (coordinates[0] + 2 * face_size, 4 * face_size - 1), "L"
            if x < 2 * face_size:
                return (
                    2 * face_size,
                    4 * face_size - (position[0] - face_size) - 1,
                ), "D"
            return (3 * face_size - position[0] - 1, 3 * face_size - 1), "L"
        case "U":
            x = coordinates[0]
            if x < face_size:
                return (face_size, face_size - (position[1] - 2 * face_size) + 1), "D"
            if x < 2 * face_size:
                return (face_size - (2 * face_size - position[1]), 2 * face_size), "R"
            return (face_size + 4 * face_size - position[1] - 1, 3 * face_size - 1), "L"
        case "D":
            x = coordinates[0]
            if x < 2 * face_size:
                return (
                    3 * face_size - 1,
                    3 * face_size - (face_size - position[1]),
                ), "U"
            return (2 * face_size - 1, 3 * face_size - position[1] - 1), "U"


orientation = start_orientation
position = start_position
for c in path:
    if isinstance(c, int):
        while c > 0:
            match orientation:
                case "L":
                    row = map_rows[position[0]]
                    row_len = len(row)
                    c -= 1
                    new_position_y = position[1] - 1
                    if new_position_y == -1:
                        looped_position, new_orientation = get_looped_coordinates(
                            position, orientation
                        )
                        if map_rows[looped_position[0]][looped_position[1]] == "#":
                            break
                        row = map_rows[looped_position[0]]
                        position = looped_position
                        orientation = new_orientation
                        continue
                    match row[new_position_y]:
                        case ".":
                            position = (position[0], new_position_y)
                        case "#":
                            break
                        case " ":
                            looped_position, new_orientation = get_looped_coordinates(
                                position, orientation
                            )
                            if map_rows[looped_position[0]][looped_position[1]] == "#":
                                break
                            row = map_rows[looped_position[0]]
                            position = looped_position
                            orientation = new_orientation
                case "R":
                    row = map_rows[position[0]]
                    row_len = len(row)
                    c -= 1
                    new_position_y = position[1] + 1
                    if new_position_y == row_len:
                        looped_position, new_orientation = get_looped_coordinates(
                            position, orientation
                        )
                        if map_rows[looped_position[0]][looped_position[1]] == "#":
                            break
                        row = map_rows[looped_position[0]]
                        position = looped_position
                        orientation = new_orientation
                        continue
                    match row[new_position_y]:
                        case ".":
                            position = (position[0], new_position_y)
                        case "#":
                            break
                        case " ":
                            looped_position, new_orientation = get_looped_coordinates(
                                position, orientation
                            )
                            if map_rows[looped_position[0]][looped_position[1]] == "#":
                                break
                            row = map_rows[looped_position[0]]
                            position = looped_position
                            orientation = new_orientation
                case "U":
                    column = map_columns[position[1]]
                    column_len = len(column)
                    c -= 1
                    new_position_x = position[0] - 1
                    if new_position_x == -1:
                        looped_position, new_orientation = get_looped_coordinates(
                            position, orientation
                        )
                        if map_columns[looped_position[1]][looped_position[0]] == "#":
                            break
                        column = map_columns[looped_position[1]]
                        position = looped_position
                        orientation = new_orientation
                        continue
                    match column[new_position_x]:
                        case ".":
                            position = (new_position_x, position[1])
                        case "#":
                            break
                        case " ":
                            looped_position, new_orientation = get_looped_coordinates(
                                position, orientation
                            )
                            if (
                                map_columns[looped_position[1]][looped_position[0]]
                                == "#"
                            ):
                                break
                            column = map_columns[looped_position[1]]
                            position = looped_position
                            orientation = new_orientation
                case "D":
                    column = map_columns[position[1]]
                    column_len = len(column)
                    c -= 1
                    new_position_x = position[0] + 1
                    if new_position_x == column_len:
                        looped_position, new_orientation = get_looped_coordinates(
                            position, orientation
                        )
                        if map_columns[looped_position[1]][looped_position[0]] == "#":
                            break
                        column = map_columns[looped_position[1]]
                        position = looped_position
                        orientation = new_orientation
                        continue
                    match column[new_position_x]:
                        case ".":
                            position = (new_position_x, position[1])
                        case "#":
                            break
                        case " ":
                            looped_position, new_orientation = get_looped_coordinates(
                                position, orientation
                            )
                            if (
                                map_columns[looped_position[1]][looped_position[0]]
                                == "#"
                            ):
                                break
                            column = map_columns[looped_position[1]]
                            position = looped_position
                            orientation = new_orientation
    else:
        orientation = orientation_map[(orientation, c)]
position = (position[0] + 1, position[1] + 1)
print(
    1000 * position[0] + 4 * position[1] + orientation_value_map[orientation]
)  # Works only for properly formatted cube
