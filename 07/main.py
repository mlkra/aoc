with open("input.txt") as f:
    terminal_output = f.read().splitlines()


def index_filesystem(terminal_output):
    filesystem = {"dirs": {}, "files": {}}
    fs = filesystem
    current_path = []
    for output_line in terminal_output:
        output_line = output_line.split()
        match output_line[0]:
            case "$":
                match output_line[1]:
                    case "cd":
                        if output_line[2] == "..":
                            current_path.pop()
                            fs = filesystem
                            for path_part in current_path:
                                fs = fs["dirs"][path_part]
                        elif output_line[2] == "/":
                            fs = filesystem
                            current_path = []
                        else:
                            fs = fs["dirs"][output_line[2]]
                            current_path.append(output_line[2])
                    case "ls":
                        pass
            case "dir":
                fs["dirs"][output_line[1]] = {"dirs": {}, "files": {}}
            case _:
                fs["files"][output_line[1]] = int(output_line[0])
    return filesystem


filesystem = index_filesystem(terminal_output)


def calculate_total_size(filesystem):
    totalsize = sum(filesystem["files"].values())
    for dir in filesystem["dirs"].values():
        totalsize += calculate_total_size(dir)
    filesystem["total_size"] = totalsize
    return totalsize


calculate_total_size(filesystem)


def calculate_total_size_sum(filesystem):
    total_size_sum = (
        filesystem["total_size"] if filesystem["total_size"] < 100000 else 0
    )
    for dir in filesystem["dirs"].values():
        total_size_sum += calculate_total_size_sum(dir)
    return total_size_sum


print(calculate_total_size_sum(filesystem))

disk_space = 70000000
required_space = 30000000
needed_space = filesystem["total_size"] - (disk_space - required_space)


def calculate_min_total_size(filesystem):
    dirs_min_total_sizes = [
        calculate_min_total_size(dir) for dir in filesystem["dirs"].values()
    ]
    dirs_min_total_sizes.append(
        filesystem["total_size"]
        if filesystem["total_size"] >= needed_space
        else disk_space
    )
    return min(dirs_min_total_sizes)


print(calculate_min_total_size(filesystem))
