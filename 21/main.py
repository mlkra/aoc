from copy import deepcopy

from sympy import diophantine, sympify

with open("input.txt") as f:
    input = f.readlines()

monkeys = {}
for line in input:
    split_line = line.split(":")
    monkey = split_line[0]
    split_line = split_line[1].strip().split()
    split_line_len = len(split_line)
    value = int(split_line[0]) if split_line_len == 1 else None
    if split_line_len == 3:
        operands = (split_line[0], split_line[2])
        operator = split_line[1]
    else:
        operands = None
        operator = None
    monkeys[monkey] = {"value": value, "operands": operands, "operator": operator}


def get_value(monkeys, monkey):
    if monkey["value"]:
        return monkey["value"]
    operands = monkey["operands"]
    value1 = get_value(monkeys, monkeys[operands[0]])
    value2 = get_value(monkeys, monkeys[operands[1]])
    match monkey["operator"]:
        case "+":
            result = value1 + value2
        case "-":
            result = value1 - value2
        case "*":
            result = value1 * value2
        case "/":
            result = value1 / value2
    monkey["value"] = result
    return monkey["value"]


print(get_value(deepcopy(monkeys), monkeys["root"]))

monkeys["humn"]["value"] = "x"
root_operands = monkeys["root"]["operands"]
monkey1 = monkeys[root_operands[0]]
monkey2 = monkeys[root_operands[1]]


def get_expression(monkeys, monkey):
    if monkey["value"]:
        return str(monkey["value"])
    operands = monkey["operands"]
    value1 = str(get_expression(monkeys, monkeys[operands[0]]))
    value2 = str(get_expression(monkeys, monkeys[operands[1]]))
    match monkey["operator"]:
        case "+":
            result = f"({value1} + {value2})"
        case "-":
            result = f"({value1} - {value2})"
        case "*":
            result = f"({value1} * {value2})"
        case "/":
            result = f"({value1} / {value2})"
    monkey["value"] = result
    return monkey["value"]


expr = f"{get_expression(deepcopy(monkeys), monkey1)} - ({get_expression(deepcopy(monkeys), monkey2)})"
expr = sympify(expr)
print(diophantine(expr))
