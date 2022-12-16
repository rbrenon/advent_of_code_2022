from pprint import pprint
from string import ascii_uppercase

def main():
    raw_input = []
    with open("input.txt") as file:
        for line in file.read().splitlines():
            line = f" {line}"
            raw_input.append(line)

    split_input = [el.split('    ') for el in raw_input]
    part_one(split_input)


def parse_move(instruction: str) -> tuple:
    split_instruction = instruction.split(' ')
    number = split_instruction[1]
    source = split_instruction[3]
    target = split_instruction[5]

    return number, source, target


def move_crates(stacks: dict, move_instructions: tuple) -> dict:
    for move in range(int(move_instructions[0])):
        crate = stacks[int(move_instructions[1])].pop()
        stacks[int(move_instructions[2])].append(crate)

    return stacks


def part_one(input_data: list[list[str]]) -> None:
    # pull crates from input
    stacks = dict()

    for row in input_data:       # input [['', ' [D]'], ...], row ['', ' [D]']
        if row == [' ']:    #  [D]
            # check for blank line between starting stack definition and moves, if it moves then break out of loop
            pass
        elif row[0].strip().startswith("move "):
            # parse the instructions
            move_instructions: tuple[int, int, int] = parse_move(row[0].strip())    # number of moves, source stack, target stack
            # feed into function to move crates 1 at a time
            stacks = move_crates(stacks, move_instructions)
        else:
            # map elements to their correct stack
            # split multiple elements into distinct list items
            elements = list()
            for items in row:
                elements.extend(items.split(']'))

            for index, element in enumerate(elements):
                if element != "":
                    element = element.strip(' ').replace('[', '').replace(']', '')
                    stack_no = index + 1
                    if element not in ascii_uppercase:
                        # row is the stack numbers - which we dont need
                        pass
                    else:
                        try:
                            # insert at beginning of list
                            stacks[stack_no].insert(0, element)
                        except KeyError as e:
                            # create a new key with list of first stack element
                            stacks.update({stack_no: [element]})

    final_stacks = str()

    for k, v in sorted(stacks.items()):
        final_stacks += v[-1]

    print(f"Part one: {final_stacks}")






def process_row(inrow: list[str]) -> list[str]:
    outrow = []
    element_number = 0
    for element in inrow:
        element = element.split(']')


if __name__ == "__main__":
    main()