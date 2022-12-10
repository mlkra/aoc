with open("input.txt") as f:
    program = f.readlines()
program = [line.strip() for line in program]
program = [[p] if p == "noop" else [p.split()[0], int(p.split()[1])] for p in program]

sprite_positions = [0] * 240

X = 1
cycle = 1
check_at_cycles = [20, 60, 100, 140, 180, 220]
signal_strength_sum = 0
for instruction in program:
    sprite_positions[cycle - 1] = X
    if cycle in check_at_cycles:
        signal_strength_sum += cycle * X
    if instruction[0] == "noop":
        cycle += 1
    else:
        sprite_positions[cycle] = X
        if cycle + 1 in check_at_cycles:
            signal_strength_sum += (cycle + 1) * X
        cycle += 2
        X += instruction[1]
print(signal_strength_sum)

for cycle, sprite_position in enumerate(sprite_positions):
    if cycle % 40 == 0:
        print()
    if sprite_position - 1 <= cycle % 40 <= sprite_position + 1:
        print("#", end="")
    else:
        print(".", end="")
    cycle += 1
