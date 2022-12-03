from string import ascii_letters


def main():
    with open("input.txt") as file:
        contents = file.read().splitlines()

    chars = [char for char in ascii_letters]

    part_one(contents, chars)
    part_two(contents, chars)


def part_one(contents: list[str], char_value: list[str]) -> None:

    sum_of_incorrect_items = 0
    for content in contents:
        split_contents_at = len(content) // 2
        front_half = content[:split_contents_at]
        back_half = content[split_contents_at:]

        for item in front_half:
            if item in back_half:
                sum_of_incorrect_items += char_value.index(item) + 1
                break

    print(f"Part one: {sum_of_incorrect_items}")    # 7878
    return


def part_two(contents: list[str], char_value: list[str]) -> None:
    group_sum = 0
    group_contents = []

    for elf_index, group_content in enumerate(contents, start=1):
        group_contents.append(group_content)
        if elf_index % 3 == 0:
            for item in group_contents[0]:
                if item in group_contents[1]:
                    if item in group_contents[2]:
                        group_sum += char_value.index(item) + 1
                        break
            group_contents = []

    print(f"Part two: {group_sum}")     # 2760
    return


if __name__ == "__main__":
    main()