from ast import literal_eval
from functools import cmp_to_key

with open("input.txt") as f:
    input = f.readlines()
input = [line.strip() for line in input]

packets = []
for line in input:
    if line:
        packets.append(literal_eval(line))
packets_pairs = []
for i in range(len(packets) // 2):
    packets_pairs.append((packets[2 * i], packets[2 * i + 1]))


def compare(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return 1
        elif left > right:
            return -1
        return 0
    if isinstance(left, list) and isinstance(right, list):
        if not left:
            return 1
        if not right:
            return -1
        len_left = len(left)
        len_right = len(right)
        for i in range(len_left):
            if i >= len_right:
                return -1
            order = compare(left[i], right[i])
            if order != 0:
                return order
        if len_left == len_right:
            return 0
        else:
            return 1
    if isinstance(left, int):
        return compare([left], right)
    if isinstance(right, int):
        return compare(left, [right])


indices_sum = 0
for i, pair in enumerate(packets_pairs):
    if compare(pair[0], pair[1]) == 1:
        indices_sum += i + 1
print(indices_sum)

divider1 = [[2]]
divider2 = [[6]]
packets.extend([divider1, divider2])
packets.sort(key=cmp_to_key(compare), reverse=True)
print((packets.index(divider1) + 1) * (packets.index(divider2) + 1))
