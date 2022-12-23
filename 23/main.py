from collections import OrderedDict

with open("input.txt") as f:
    input = f.readlines()
original_elves = set()
for i, row in enumerate(input):
    for j, elf in enumerate(row):
        if elf == "#":
            original_elves.add((j, i))

neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]


def get_directions():
    directions = OrderedDict.fromkeys([(0, -1), (0, 1), (-1, 0), (1, 0)])
    directions[(0, -1)] = [(0, -1), (1, -1), (-1, -1)]
    directions[(0, 1)] = [(0, 1), (1, 1), (-1, 1)]
    directions[(-1, 0)] = [(-1, 0), (-1, -1), (-1, 1)]
    directions[(1, 0)] = [(1, 0), (1, -1), (1, 1)]
    return directions


directions = get_directions()
elves = original_elves.copy()


def get_new_positions(directions, elves):
    new_positions = {}
    for elf in elves:
        empty = True
        for neighbor in neighbors:
            if (elf[0] + neighbor[0], elf[1] + neighbor[1]) in elves:
                empty = False
                break
        if empty:
            continue
        for direction, to_check in directions.items():
            empty = True
            for delta in to_check:
                if (elf[0] + delta[0], elf[1] + delta[1]) in elves:
                    empty = False
            if not empty:
                continue
            new_position = (elf[0] + direction[0], elf[1] + direction[1])
            if new_position in new_positions:
                new_positions[new_position].append(elf)
            else:
                new_positions[new_position] = [elf]
            break
    return new_positions


for _ in range(10):
    first_direction = next(iter(directions))
    new_positions = get_new_positions(directions, elves)
    for new_position, old_positions in new_positions.items():
        if len(old_positions) == 1:
            elves.remove(old_positions[0])
            elves.add(new_position)
    directions.move_to_end(first_direction)

rectangle_start = (min([elf[0] for elf in elves]), min([elf[1] for elf in elves]))
rectangle_end = (max([elf[0] for elf in elves]), max([elf[1] for elf in elves]))
empty_tiles = 0
for i in range(rectangle_start[0], rectangle_end[0] + 1):
    for j in range(rectangle_start[1], rectangle_end[1] + 1):
        if (i, j) not in elves:
            empty_tiles += 1
print(empty_tiles)

directions = get_directions()
elves = original_elves.copy()
round = 0
while True:
    round += 1
    first_direction = next(iter(directions))
    new_positions = get_new_positions(directions, elves)
    moved = False
    for new_position, old_positions in new_positions.items():
        if len(old_positions) == 1:
            elves.remove(old_positions[0])
            elves.add(new_position)
        moved = True
    directions.move_to_end(first_direction)
    if not moved:
        break
print(round)
