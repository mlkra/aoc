from collections import defaultdict, deque

with open("input.txt") as f:
    input = f.readlines()
input = [line.strip() for line in input]

blizzards_directions = {
    "^": (0, -1),
    "v": (0, 1),
    "<": (-1, 0),
    ">": (1, 0),
}
column_len = len(input) - 2
row_len = len(input[0]) - 2

start = (0, -1)
end = (row_len - 1, column_len)


def get_blizzards():
    blizzards = defaultdict(list)
    for j, row in enumerate(input):
        if j == 0 or j == column_len + 1:
            continue
        for i, c in enumerate(input[j]):
            if i == 0 or i == row_len + 1:
                continue
            if c != ".":
                blizzards[(i - 1, j - 1)].append(c)
    return blizzards


def generate_moves(coord):
    i, j = coord
    yield i, j
    if coord == start:
        yield i, j + 1
        return
    elif coord == end:
        yield end[0], end[1] - 1
        return
    elif coord == (end[0], end[1] - 1):
        yield end
    elif coord == (start[0], start[1] + 1):
        yield start
    if i > 0:
        yield i - 1, j
    if j > 0:
        yield i, j - 1
    if i < row_len - 1:
        yield i + 1, j
    if j < column_len - 1:
        yield i, j + 1


def get_min_time():
    max_time = 0
    coords = [end]
    # coords.extend([start, end])
    queue = deque([(start, 1, coords)])
    blizzards = get_blizzards()
    while queue:
        pos, t, coord = queue.popleft()
        if t > max_time:
            states = set([])
            new_blizzards = defaultdict(list)
            for blizzard, directions in blizzards.items():
                x, y = blizzard
                for dir in directions:
                    new_blizzard = tuple(
                        [
                            (x + blizzards_directions[dir][0]) % row_len,
                            (y + blizzards_directions[dir][1]) % column_len,
                        ]
                    )
                    new_blizzards[new_blizzard].append(dir)
            blizzards = new_blizzards
            max_time = t
        for move in generate_moves(pos):
            if move == coord[0]:
                coord = list(coord[1:])
                if len(coord) == 0:
                    return t
                queue = deque([(move, t + 1, coord)])
            elif move not in states and move not in blizzards:
                states.add(move)
                queue.append((move, t + 1, coord))


print(get_min_time())
