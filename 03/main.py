rucksacks = []
rucksacks_compartmentalized = []
with open("input.txt") as f:
    for line in f:
        line = line.strip()
        rucksacks.append(line)
        rucksacks_compartmentalized.append(
            (line[: len(line) // 2], line[len(line) // 2 :])
        )


def get_item_priority(item):
    if item.islower():
        priority = ord(item) - 96
    else:
        priority = ord(item) - 38
    return priority


priorities = []
for rucksack_compartment1, rucksack_compartment2 in rucksacks_compartmentalized:
    items = {item for item in rucksack_compartment1}
    for item in rucksack_compartment2:
        if item in items:
            priorities.append(get_item_priority(item))
            break
print(sum(priorities))

priorities = []
for i in range(len(rucksacks) // 3):
    items = {}
    rucksack = rucksacks[3 * i]
    for item in rucksack:
        items[item] = 1
    rucksack = rucksacks[3 * i + 1]
    for item in rucksack:
        if item in items:
            items[item] = 2
    rucksack = rucksacks[3 * i + 2]
    for item in rucksack:
        if item in items and items[item] == 2:
            priorities.append(get_item_priority(item))
            break
print(sum(priorities))
