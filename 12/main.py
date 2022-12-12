from itertools import product

from networkx import DiGraph, NetworkXNoPath, shortest_path_length

with open("input.txt") as f:
    input = f.readlines()
heightmap = [list(line.strip()) for line in input]

len_y = len(heightmap)
len_x = len(heightmap[0])
start_node = None
end_node = None
graph = DiGraph()
for i in range(len_y):
    for j in range(len_x):
        graph.add_node((i, j))
        if heightmap[i][j] == "S":
            start_node = (i, j)
            heightmap[i][j] = "a"
        elif heightmap[i][j] == "E":
            end_node = (i, j)
            heightmap[i][j] = "z"
for i in range(len_y):
    for j in range(len_x):
        height = ord(heightmap[i][j])
        if i > 0:
            new_height = ord(heightmap[i - 1][j])
            if new_height <= height + 1:
                graph.add_edge((i, j), (i - 1, j))
        if i < len_y - 1:
            new_height = ord(heightmap[i + 1][j])
            if new_height <= height + 1:
                graph.add_edge((i, j), (i + 1, j))
        if j > 0:
            new_height = ord(heightmap[i][j - 1])
            if new_height <= height + 1:
                graph.add_edge((i, j), (i, j - 1))
        if j < len_x - 1:
            new_height = ord(heightmap[i][j + 1])
            if new_height <= height + 1:
                graph.add_edge((i, j), (i, j + 1))

print(shortest_path_length(graph, start_node, end_node))

start_nodes = [
    (i, j) for i, j in product(range(len_y), range(len_x)) if heightmap[i][j] == "a"
]
min_path_len = len_x * len_y
for start_node in start_nodes:
    try:
        path_len = shortest_path_length(graph, start_node, end_node)
        min_path_len = min(min_path_len, path_len)
    except NetworkXNoPath:
        pass
print(min_path_len)
