with open("input.txt") as f:
    lines = [l.strip().split() for l in f.readlines()]
rope_motions = [[row[0], int(row[1])] for row in lines]


def move_head(head, direction):
    match direction:
        case "U":
            head = (head[0], head[1] + 1)
        case "D":
            head = (head[0], head[1] - 1)
        case "L":
            head = (head[0] - 1, head[1])
        case "R":
            head = (head[0] + 1, head[1])
    return head


def move_tail(head, tail):
    if not (
        tail[0] - 1 <= head[0] <= tail[0] + 1 and tail[1] - 1 <= head[1] <= tail[1] + 1
    ):
        if tail[0] == head[0] + 2 and tail[1] == head[1]:
            tail = (tail[0] - 1, tail[1])
        elif tail[0] == head[0] - 2 and tail[1] == head[1]:
            tail = (tail[0] + 1, tail[1])
        elif tail[0] == head[0] and tail[1] == head[1] + 2:
            tail = (tail[0], tail[1] - 1)
        elif tail[0] == head[0] and tail[1] == head[1] - 2:
            tail = (tail[0], tail[1] + 1)
        elif tail[0] == head[0] + 1 and tail[1] == head[1] + 2:
            tail = (tail[0] - 1, tail[1] - 1)
        elif tail[0] == head[0] + 1 and tail[1] == head[1] - 2:
            tail = (tail[0] - 1, tail[1] + 1)
        elif tail[0] == head[0] - 1 and tail[1] == head[1] + 2:
            tail = (tail[0] + 1, tail[1] - 1)
        elif tail[0] == head[0] - 1 and tail[1] == head[1] - 2:
            tail = (tail[0] + 1, tail[1] + 1)
        elif tail[0] == head[0] + 2 and tail[1] == head[1] + 1:
            tail = (tail[0] - 1, tail[1] - 1)
        elif tail[0] == head[0] + 2 and tail[1] == head[1] - 1:
            tail = (tail[0] - 1, tail[1] + 1)
        elif tail[0] == head[0] - 2 and tail[1] == head[1] + 1:
            tail = (tail[0] + 1, tail[1] - 1)
        elif tail[0] == head[0] - 2 and tail[1] == head[1] - 1:
            tail = (tail[0] + 1, tail[1] + 1)
        elif tail[0] == head[0] + 2 and tail[1] == head[1] + 2:
            tail = (tail[0] - 1, tail[1] - 1)
        elif tail[0] == head[0] + 2 and tail[1] == head[1] - 2:
            tail = (tail[0] - 1, tail[1] + 1)
        elif tail[0] == head[0] - 2 and tail[1] == head[1] + 2:
            tail = (tail[0] + 1, tail[1] - 1)
        elif tail[0] == head[0] - 2 and tail[1] == head[1] - 2:
            tail = (tail[0] + 1, tail[1] + 1)
    return tail


def get_number_of_unique_positions_visited_by_tail(rope_length):
    initial_position = (0, 0)
    positions = [initial_position] * rope_length
    visited_positions = {initial_position}
    for motion in rope_motions:
        direction = motion[0]
        steps = motion[1]
        for _ in range(steps):
            positions[0] = move_head(positions[0], direction)
            for i in range(len(positions) - 1):
                positions[i + 1] = move_tail(positions[i], positions[i + 1])
            visited_positions.add(positions[-1])
    return len(visited_positions)


print(get_number_of_unique_positions_visited_by_tail(2))

print(get_number_of_unique_positions_visited_by_tail(10))
