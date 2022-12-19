import re
from collections import deque
from enum import Enum
from math import inf

with open("input.txt") as f:
    input = f.readlines()


class ResourceType(Enum):
    ORE = 0
    CLAY = 1
    OBSIDIAN = 2
    GEODE = 3


blueprints = []
for line in input:
    numbers = re.findall("[0-9]+", line)
    blueprints.append(
        {
            ResourceType.ORE: (int(numbers[1]), 0, 0, 0),
            ResourceType.CLAY: (int(numbers[2]), 0, 0, 0),
            ResourceType.OBSIDIAN: (int(numbers[3]), int(numbers[4]), 0, 0),
            ResourceType.GEODE: (int(numbers[5]), 0, int(numbers[6]), 0),
        }
    )

resources = []
for resource_type in ResourceType:
    resources.extend([blueprint[resource_type] for blueprint in blueprints])
max_costs = (
    max(r[0] for r in resources),
    max(r[1] for r in resources),
    max(r[2] for r in resources),
    inf,
)


def can_build_robot(resources, required_resources):
    return all(
        resource >= required
        for resource, required in zip(resources, required_resources)
    )


def spend_resources_for_robot(resources, required_resources):
    assert can_build_robot(resources, required_resources)
    return tuple(
        resource - required for resource, required in zip(resources, required_resources)
    )


def collect_resources(robots, resources):
    return tuple(resource + robot for robot, resource in zip(robots, resources))


def build_robot(robots, robot_index):
    return tuple(robot + (i == robot_index) for i, robot in enumerate(robots))


def throw_extra_resources(resources):
    return tuple(
        min(resource, 2 * cost) for resource, cost in zip(resources, max_costs)
    )


def get_max_geodes(blueprint, allocated_time):
    initial = ((1, 0, 0, 0), (0, 0, 0, 0))
    visited = set()
    queue = deque()
    time = 0
    queue.append(initial)
    while queue and time < allocated_time:
        for _ in range(len(queue)):
            state = queue.popleft()
            if state in visited:
                continue
            visited.add(state)
            robots, resources = state
            if can_build_robot(resources, blueprint[ResourceType.GEODE]):
                new_resources = throw_extra_resources(
                    collect_resources(
                        robots,
                        spend_resources_for_robot(
                            resources, blueprint[ResourceType.GEODE]
                        ),
                    )
                )
                new_robots = build_robot(robots, ResourceType.GEODE.value)
                queue.append((new_robots, new_resources))
            else:
                for robot_type in ResourceType:
                    if robots[robot_type.value] >= max_costs[robot_type.value]:
                        continue
                    if can_build_robot(resources, blueprint[robot_type]):
                        new_resources = throw_extra_resources(
                            collect_resources(
                                robots,
                                spend_resources_for_robot(
                                    resources, blueprint[robot_type]
                                ),
                            )
                        )
                        new_robots = build_robot(robots, robot_type.value)
                        queue.append((new_robots, new_resources))
                new_resources = throw_extra_resources(
                    collect_resources(robots, resources)
                )
                queue.append((robots, new_resources))
        time += 1

    geodes = [resources[ResourceType.GEODE.value] for _, resources in queue]
    return max(geodes)


allocated_time = 24
print(
    sum(
        [
            (i + 1) * get_max_geodes(blueprint, allocated_time)
            for i, blueprint in enumerate(blueprints)
        ]
    )
)


allocated_time = 32
mul = 1
for blueprint in blueprints[:3]:
    mul *= get_max_geodes(blueprint, allocated_time)
print(mul)
