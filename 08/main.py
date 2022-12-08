with open("input.txt") as f:
    lines = [list(l.strip()) for l in f.readlines()]
trees = [[int(tree) for tree in row] for row in lines]

trees_length = len(trees)

visible_trees = 4 * (trees_length - 1)
for i in range(1, trees_length - 1):
    for j in range(1, trees_length - 1):
        visible = False
        tree = trees[i][j]
        if max([trees[k][j] for k in range(i)]) < tree:
            visible = True
        if max([trees[k][j] for k in range(i + 1, trees_length)]) < tree:
            visible = True
        if max([trees[i][k] for k in range(j)]) < tree:
            visible = True
        if max([trees[i][k] for k in range(j + 1, trees_length)]) < tree:
            visible = True
        if visible:
            visible_trees += 1
print(visible_trees)

max_scenic_score = 0
for i in range(1, trees_length - 1):
    for j in range(1, trees_length - 1):
        up = 0
        down = 0
        left = 0
        right = 0
        tree = trees[i][j]
        for k in range(i - 1, -1, -1):
            up += 1
            if trees[k][j] >= tree:
                break
        for k in range(i + 1, trees_length):
            down += 1
            if trees[k][j] >= tree:
                break
        for k in range(j - 1, -1, -1):
            left += 1
            if trees[i][k] >= tree:
                break
        for k in range(j + 1, trees_length):
            right += 1
            if trees[i][k] >= tree:
                break
        scenic_score = up * down * left * right
        max_scenic_score = max(max_scenic_score, scenic_score)
print(max_scenic_score)
