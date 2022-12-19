from pprint import pprint


def main():
    with open("input.txt") as file:
        infile = file.read().splitlines()

    part_one(infile)


def part_one(cli: str) -> None:
    filesystem = dict()
    dir_key = "/"
    for line in cli:
        if line.startswith("$ cd"):  # changing directory
            destination_dir = line.split()[-1]  # directory
            if destination_dir == "/":
                dir_key = "/"
            elif destination_dir == "..":
                dir_key = (
                    dir_key[0: (dir_key.rfind("/", 0, len(dir_key) - 1))] + "/"
                )  # find the last '/' beside end
            else:
                dir_key += destination_dir + "/"
        elif line.startswith("dir "):
            pass
        elif line.startswith("$ ls"):
            pass
        else:
            filesize, filename = line.split(" ")
            try:
                filesystem[dir_key]["files"].append((int(filesize), filename))
                filesystem[dir_key]["dir_size"] += int(filesize)
            except KeyError as ke:
                filesystem[dir_key] = {"files": [], "dir_size": int(filesize)}
                filesystem[dir_key]["files"].append((int(filesize), filename))
            # check if it's the root directory otherwise add file size to subdirs dir_size
            # sub_dir = (dir_key[0: (dir_key.rfind("/", 0, len(dir_key) - 1))] + "/")
            sub_dir = dir_key
            while sub_dir != '/':
                sub_dir = (sub_dir[0: (sub_dir.rfind("/", 0, len(sub_dir) - 1))] + "/")
                try:
                    filesystem[sub_dir]["files"].append((int(filesize), filename))
                    filesystem[sub_dir]["dir_size"] += int(filesize)
                except KeyError as e:
                    filesystem[sub_dir] = {"files": [], "dir_size": int(filesize)}
                    filesystem[sub_dir]["files"].append((int(filesize), filename))

    sum_of_dirs_under_100k = 0

    # for each dictionary key see if the size is < 100,000,
    # if it is check if that key is found in any other keys where size is < 100k
    for fs_dir_key in filesystem.keys():
        # check if the current directory is less than 100k
        if filesystem[fs_dir_key]["dir_size"] <= 100_000:
            sum_of_dirs_under_100k += filesystem[fs_dir_key]["dir_size"]

    print(f"Part one: {sum_of_dirs_under_100k}")    # answer: 1_845_346; high: 3_047_297, 2_601_855; low: 1_779_072
    print(f"Part two: {part_two(filesystem)}")      # answer: 3_636_703; high: 38_090_606


def part_two(filesystem: dict) -> str:
    total_disk_size: int = 70_000_000
    unused_space_needed: int = 30_000_000

    min_dir_size_to_be_deleted = unused_space_needed - (total_disk_size - filesystem['/']['dir_size'])

    dir_to_be_deleted = list()
    for directory in filesystem:
        if filesystem[directory]['dir_size'] >= min_dir_size_to_be_deleted:
            dir_to_be_deleted.append(filesystem[directory]['dir_size'])

    return sorted(dir_to_be_deleted)[0]


if __name__ == "__main__":
    main()
