

def main():
    with open("input.txt") as file:
        raw_input = file.read().splitlines()

    print(part_one(raw_input))


def part_one(input_data):
    elfs_cals: list[int] = []
    calorie_count: int = 0
    elf_count = 1

    for calorie_line in input_data:
        if calorie_line == '':
            elfs_cals.append(calorie_count)
            calorie_count = 0
            elf_count += 1
        else:
            calorie_count += int(calorie_line)

    p1 = max(elfs_cals)     # 70509
    p2 = sum((sorted(elfs_cals, reverse=True))[0:3])    # 208567

    return f"Part 1: {p1} Part 2: {p2} Total elves = {elf_count}"


if __name__ == "__main__":
    main()