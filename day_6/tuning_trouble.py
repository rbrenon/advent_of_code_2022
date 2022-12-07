from collections import defaultdict


P1_MARKER: int = 4
P2_MARKER: int = 14

def main():
    with open("input.txt") as file:
        raw_input = file.read()

    print(f"Part One: {part_one(raw_input, P1_MARKER)}")
    print(f"Part Two: {part_one(raw_input, P2_MARKER)}")


def part_one(datastream: str, marker_length: int) -> int:

    for index, _ in enumerate(datastream):
        char_count = defaultdict(int)
        try:
            char_check = list(datastream[index:index+marker_length])
            for char in char_check:
                char_count[char] += 1
            if len(char_count) == marker_length:
                break
        except KeyError as e:
            break

    return index + marker_length


if __name__ == "__main__":
    main()