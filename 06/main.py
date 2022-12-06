with open("input.txt") as f:
    datastream = list(f.readline())


def find_marker(datastream, marker_length):
    for i in range(len(datastream) - marker_length):
        if len(set(datastream[i : i + marker_length])) == len(
            datastream[i : i + marker_length]
        ):
            return i + marker_length


print(find_marker(datastream, 4))

print(find_marker(datastream, 14))
