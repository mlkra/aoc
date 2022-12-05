from copy import deepcopy

original_stacks = [
    ["Q", "S", "W", "C", "Z", "V", "F", "T"],
    ["Q", "R", "B"],
    ["B", "Z", "T", "Q", "P", "M", "S"],
    ["D", "V", "F", "R", "Q", "H"],
    ["J", "G", "L", "D", "B", "S", "T", "P"],
    ["W", "R", "T", "Z"],
    ["H", "Q", "M", "N", "S", "F", "R", "J"],
    ["R", "N", "F", "H", "W"],
    ["J", "Z", "T", "Q", "P", "R", "B"],
]
with open("input.txt") as f:
    lines = [l.strip().split() for l in f.readlines()]
lines = lines[10:]
instructions = [(int(line[1]), int(line[3]) - 1, int(line[5]) - 1) for line in lines]

stacks = deepcopy(original_stacks)
for count, from_, to in instructions:
    for _ in range(count):
        stacks[to].append(stacks[from_].pop())
print("".join([stack[-1] for stack in stacks]))

stacks = deepcopy(original_stacks)
for count, from_, to in instructions:
    stacks[to].extend(stacks[from_][-count:])
    del stacks[from_][-count:]
print("".join([stack[-1] for stack in stacks]))
