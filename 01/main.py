inventories = []
with open("input.txt") as f:
    inventory = []
    for line in f:
        if line == "\n":
            inventories.append(inventory)
            inventory = []
        else:
            inventory.append(int(line))
    inventories.append(inventory)

inventories = [sum(inventory) for inventory in inventories]
print(max(inventories))

inventories = sorted(inventories)
print(sum(inventories[-3:]))
