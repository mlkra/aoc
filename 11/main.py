from copy import deepcopy
from enum import Enum

with open("input.txt") as f:
    input = f.readlines()
input = [line.strip() for line in input]


class Operation(Enum):
    ADD = 1
    MUL = 2


monkeys_count = 8

monkeys = []
for i in range(monkeys_count):
    items = input[7 * i + 1][16:].split(", ")
    items = [int(item) for item in items]
    operation = Operation.ADD if input[7 * i + 2][21] == "+" else Operation.MUL
    operand = None if input[7 * i + 2][23:] == "old" else int(input[7 * i + 2][23:])
    check = int(input[7 * i + 3][19:])
    monkey_true = int(input[7 * i + 4][25:])
    monkey_false = int(input[7 * i + 5][26:])
    monkeys.append(
        {
            "items": items,
            "operation": operation,
            "operand": operand,
            "test": {
                "check": check,
                True: monkey_true,
                False: monkey_false,
            },
        }
    )
checks = [monkey["test"]["check"] for monkey in monkeys]
mul = 1
for check in checks:
    mul *= check


def calculate_monkey_business(monkeys_count, rounds, divide_worry_level=True):
    inspected_items = [0] * monkeys_count
    current_monkeys = deepcopy(monkeys)
    for _ in range(rounds):
        for i, monkey in enumerate(current_monkeys):
            for item in monkey["items"]:
                inspected_items[i] += 1
                operand = item if monkey["operand"] is None else monkey["operand"]
                if monkey["operation"] == Operation.ADD:
                    item += operand
                else:
                    item *= operand
                if divide_worry_level:
                    item //= 3
                item %= mul
                test = item % monkey["test"]["check"] == 0
                next_monkey = monkey["test"][test]
                current_monkeys[next_monkey]["items"].append(item)
            monkey["items"] = []
    inspected_items = sorted(inspected_items, reverse=True)
    return inspected_items[0] * inspected_items[1]


print(calculate_monkey_business(monkeys_count, 20))

print(calculate_monkey_business(monkeys_count, 10000, False))
