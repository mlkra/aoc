with open("input.txt") as f:
    input = f.readlines()
encrypted_coordinates = [int(line.strip()) for line in input]
encrypted_coordinates_len = len(encrypted_coordinates)
indexed_coordinates = list(enumerate(encrypted_coordinates))


def mix_coordinates(indexed_coordinates, mixed_indexed_coordinates):
    for indexed_coordinate in indexed_coordinates:
        coordinate = indexed_coordinate[1]
        old_index = mixed_indexed_coordinates.index(indexed_coordinate)
        new_index = (old_index + coordinate) % (encrypted_coordinates_len - 1)
        if old_index == new_index:
            continue
        mixed_indexed_coordinates = (
            mixed_indexed_coordinates[:old_index]
            + mixed_indexed_coordinates[old_index + 1 :]
        )
        mixed_indexed_coordinates = (
            mixed_indexed_coordinates[:new_index]
            + [indexed_coordinate]
            + mixed_indexed_coordinates[new_index:]
        )
    return mixed_indexed_coordinates


mixed_indexed_coordinates = mix_coordinates(indexed_coordinates, indexed_coordinates[:])


def get_zero_index(coordinates):
    for i, coord in enumerate(coordinates):
        if coord[1] == 0:
            return i


def print_result(mixed_indexed_coordinates):
    print(
        sum(
            [
                mixed_indexed_coordinates[
                    (get_zero_index(mixed_indexed_coordinates) + i)
                    % encrypted_coordinates_len
                ][1]
                for i in [1000, 2000, 3000]
            ]
        )
    )


print_result(mixed_indexed_coordinates)

decryption_key = 811589153
encrypted_coordinates = [coord * decryption_key for coord in encrypted_coordinates]
indexed_coordinates = list(enumerate(encrypted_coordinates))

mixed_indexed_coordinates = indexed_coordinates[:]
for _ in range(10):
    mixed_indexed_coordinates = mix_coordinates(
        indexed_coordinates, mixed_indexed_coordinates
    )
print_result(mixed_indexed_coordinates)
