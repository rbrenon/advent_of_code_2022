def main():
    with open("input.txt") as file:
        raw_input = file.read().splitlines()  # ['71-89,66-70', '24-70,23-55, ...]

    part_one(raw_input)
    part_two(raw_input)


def part_one(cleanup_coords: list[str]) -> None:
    overlapping_coordinates = 0

    for coord in cleanup_coords:  # ['71-89,66-70', ...]
        elf_one_coord_str, elf_two_coord_str = coord.split(",")  # '71-89' ,'66-70'
        elf_one_coord_list = elf_one_coord_str.split("-")  # ['71', '89']
        elf_two_coord_list = elf_two_coord_str.split("-")  # ['66', '70']

        if (
            int(elf_one_coord_list[0]) >= int(elf_two_coord_list[0])
            and int(elf_one_coord_list[1]) <= int(elf_two_coord_list[1])
        ) or (
            int(elf_two_coord_list[0]) >= int(elf_one_coord_list[0])
            and int(elf_two_coord_list[1]) <= int(elf_one_coord_list[1])
        ):
            overlapping_coordinates += 1

    print(f"Part One: {overlapping_coordinates}")  # 573


def part_two(cleanup_coords: list[str]) -> None:
    overlapping_coordinates = 0

    for coord in cleanup_coords:  # ['71-89,66-70', ...]
        elf_one_coord_str, elf_two_coord_str = coord.split(",")  # '71-89' ,'66-70'
        elf_one_coord_list = elf_one_coord_str.split("-")  # ['71', '89']
        elf_two_coord_list = elf_two_coord_str.split("-")  # ['66', '70']

        if (
                int(elf_two_coord_list[0]) <= int(elf_one_coord_list[0]) <= int(elf_two_coord_list[1])
        ) or (
                int(elf_two_coord_list[0]) <= int(elf_one_coord_list[1]) <= int(elf_two_coord_list[1])
        ) or (
                int(elf_one_coord_list[0]) <= int(elf_two_coord_list[0]) <= int(elf_one_coord_list[1])
        ) or (
                int(elf_one_coord_list[0]) <= int(elf_two_coord_list[1]) <= int(elf_one_coord_list[1])

        ):
            overlapping_coordinates += 1

    print(f"Part Two: {overlapping_coordinates}")  # too low: 757


if __name__ == "__main__":
    main()
