import re

with open("input.txt") as f:
    input = f.readlines()
input = [line.strip() for line in input]

sensor_beacon_map = {}
for line in input:
    coordinates = re.findall("-*\d+", line)
    sensor = (int(coordinates[0]), int(coordinates[1]))
    beacon = (int(coordinates[2]), int(coordinates[3]))
    sensor_beacon_map[sensor] = beacon


def taxicab_distance(x, y):
    return abs(y[0] - x[0]) + abs(y[1] - x[1])


sensor_range_map = {}
for sensor, beacon in sensor_beacon_map.items():
    sensor_range_map[sensor] = taxicab_distance(sensor, beacon)

checked_row = 2000000
row_coverage = set()
for sensor, sensor_range in sensor_range_map.items():
    beacon_x = sensor[0]
    checked_point = (beacon_x, checked_row)
    if taxicab_distance(sensor, checked_point) <= sensor_range:
        row_coverage.add(checked_point)
        while True:
            checked_point = (checked_point[0] - 1, checked_row)
            if taxicab_distance(sensor, checked_point) <= sensor_range:
                row_coverage.add(checked_point)
            else:
                break
        checked_point = (beacon_x, checked_row)
        while True:
            checked_point = (checked_point[0] + 1, checked_row)
            if taxicab_distance(sensor, checked_point) <= sensor_range:
                row_coverage.add(checked_point)
            else:
                break
row_coverage = row_coverage.difference(sensor_beacon_map.values())
print(len(row_coverage))

min_xy = 0
max_xy = 4000000
rows_coverage = []
for i in range(min_xy, max_xy):
    sensor_coverage = []
    for sensor, sensor_range in sensor_range_map.items():
        distance = taxicab_distance(sensor, (sensor[0], i))
        if distance <= sensor_range:
            available_range = sensor_range - distance
            if (
                sensor[0] + available_range > min_xy
                and sensor[0] - available_range < max_xy
            ):
                sensor_coverage.append(
                    (
                        max(min_xy, sensor[0] - available_range),
                        min(max_xy, sensor[0] + available_range),
                    )
                )
    rows_coverage.append(sensor_coverage)
new_rows_coverage = []
for row_coverage in rows_coverage:
    new_row_coverage = []
    for begin, end in sorted(row_coverage):
        if new_row_coverage and new_row_coverage[-1][1] >= begin - 1:
            new_row_coverage[-1][1] = max(new_row_coverage[-1][1], end)
        else:
            new_row_coverage.append([begin, end])
    new_rows_coverage.append(new_row_coverage)
for y, row_coverage in enumerate(new_rows_coverage):
    if len(row_coverage) > 1:
        x = row_coverage[0][1] + 1
        print(x * 4000000 + y)
        break
