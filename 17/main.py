rock_types = [
    [
        0b000111100,
    ],
    [
        0b000010000,
        0b000111000,
        0b000010000,
    ],
    [
        0b000001000,
        0b000001000,
        0b000111000,
    ],
    [
        0b000100000,
        0b000100000,
        0b000100000,
        0b000100000,
    ],
    [
        0b000110000,
        0b000110000,
    ],
]

with open("input.txt") as f:
    input = f.readline().strip()
jet_pattern = tuple(input)

chamber_width = 7
chamber_empty_row = 0b100000001


def count_active_bits(n: int) -> int:
    return bin(n).count("1")


def rock_can_move(chamber: list[int], rock, rock_rows) -> bool:
    if rock_rows[0] < 0:
        return False
    chamber_len = len(chamber)
    if chamber_len < rock_rows[1] + 1:
        for _ in range(rock_rows[1] + 1 - chamber_len):
            chamber.append(chamber_empty_row)
    for i in range(0, len(rock)):
        chamber_row = chamber[rock_rows[1] - i]
        new_row = chamber_row ^ rock[i]
        if count_active_bits(new_row) != count_active_bits(
            chamber_row
        ) + count_active_bits(rock[i]):
            return False
    return True


def jet_move(rock, chamber, jet_iterator, rock_rows):
    jet = jet_pattern[jet_iterator]
    jet_iterator += 1
    jet_iterator %= len(jet_pattern)
    if jet == "<":
        new_rock = [row << 1 for row in rock]
        if rock_can_move(chamber, new_rock, rock_rows):
            rock = new_rock
    else:
        new_rock = [row >> 1 for row in rock]
        if rock_can_move(chamber, new_rock, rock_rows):
            rock = new_rock
    return rock, jet_iterator


def down_move(chamber, rock, rock_rows):
    new_rock_rows = (rock_rows[0] - 1, rock_rows[1] - 1)
    if rock_can_move(chamber, rock, new_rock_rows):
        return True, new_rock_rows
    return False, rock_rows


def simulate_one_rock(rock, chamber: list[int], tower_height: int, jet_iterator: int):
    start_row = tower_height + 3
    end_row = tower_height + 3 + len(rock) - 1
    rock_rows = (start_row, end_row)
    while True:
        rock, jet_iterator = jet_move(rock, chamber, jet_iterator, rock_rows)
        moved, rock_rows = down_move(chamber, rock, rock_rows)
        if not moved:
            for j in range(len(rock) - 1, -1, -1):
                chamber[rock_rows[1] - j] ^= rock[j]
            tower_height = max(tower_height, rock_rows[1] + 1)
            return rock, chamber, tower_height, jet_iterator


def simulate_rocks(rock_types, simulate_one_rock, number_of_rocks):
    tower_height = 0
    chamber = []
    jet_iterator = 0
    for i in range(number_of_rocks):
        rock_type_index = i % len(rock_types)
        rock = rock_types[rock_type_index][:]
        rock, chamber, tower_height, jet_iterator = simulate_one_rock(
            rock, chamber, tower_height, jet_iterator
        )
    print(tower_height)


number_of_rocks = 2022
simulate_rocks(rock_types, simulate_one_rock, number_of_rocks)

number_of_rocks = 1000000000000
simulate_rocks(rock_types, simulate_one_rock, number_of_rocks)
