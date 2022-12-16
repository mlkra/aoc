import re
from functools import cache

from networkx import Graph, shortest_path_length

with open("input.txt") as f:
    input = f.readlines()
valves_data = {}
for line in input:
    valve = line[6:8]
    flow_rate = int(re.search("\d+", line).group(0))
    tunnels = re.findall("[A-Z]{2}", line)[1:]
    valves_data[valve] = {
        "flow_rate": flow_rate,
        "tunnels": tunnels,
    }
start = "AA"
time_to_eruption = 30

tunnels_graph = Graph()
for source, valve_data in valves_data.items():
    for target in valve_data["tunnels"]:
        tunnels_graph.add_edge(source, target)


def _add_distance(distances, source, target, distance):
    if source in distances:
        distances[source][target] = distance
    else:
        distances[source] = {target: distance}


distances = {}
valves = list(valves_data.keys())
for i, source in enumerate(valves):
    if valves_data[source]["flow_rate"] > 0 or source == start:
        for target in valves[i + 1 :]:
            if valves_data[target]["flow_rate"] > 0 or target == start:
                shortest_path_len = shortest_path_length(tunnels_graph, source, target)
                _add_distance(distances, source, target, shortest_path_len)
                _add_distance(distances, target, source, shortest_path_len)

max_released_pressure = 0


def dfs(valve, opened, time=0, released_pressure=0):
    global max_released_pressure
    opened.add(valve)
    for neighbor, distance in distances[valve].items():
        if neighbor not in opened:
            new_time = time + distance + 1
            if new_time < time_to_eruption:
                new_released_pressure = released_pressure + valves_data[neighbor][
                    "flow_rate"
                ] * (time_to_eruption - new_time)
                max_released_pressure = max(
                    max_released_pressure, new_released_pressure
                )
                dfs(neighbor, opened.copy(), new_time, new_released_pressure)


opened = set()
dfs(start, opened)
print(max_released_pressure)

time_to_eruption = 26
working_valves = set(distances.keys())
working_valves = working_valves.difference("AA")


@cache
def dfs2(valve_human, valve_elephant, opened, time0=0, time1=0):
    max_released_pressure = 0
    closed_valves = working_valves.difference(opened)
    for valve in closed_valves:
        if valve not in opened:
            new_opened = tuple(sorted([*opened, valve]))
            flow_rate = valves_data[valve]["flow_rate"]
            if valve in distances[valve_human]:
                new_time0 = time0 + distances[valve_human][valve] + 1
                if new_time0 <= time_to_eruption:
                    human_max = dfs2(
                        valve, valve_elephant, new_opened, new_time0, time1
                    ) + flow_rate * (time_to_eruption - new_time0)
                    max_released_pressure = max(max_released_pressure, human_max)
            if valve in distances[valve_elephant]:
                new_time1 = time1 + distances[valve_elephant][valve] + 1
                if new_time1 <= time_to_eruption:
                    elephant_max = dfs2(
                        valve_human, valve, new_opened, time0, new_time1
                    ) + flow_rate * (time_to_eruption - new_time1)
                    max_released_pressure = max(max_released_pressure, elephant_max)
    return max_released_pressure


print(dfs2(start, start, ()))
