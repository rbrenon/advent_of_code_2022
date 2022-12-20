def main():
    with open("input.txt") as file:
        file_contents = file.read().splitlines()

    tree_matrix = [
        [int(tree) for tree in file_contents[row_index]]
        for row_index, row in enumerate(file_contents)
    ]

    print(f"Part one: {part_one(tree_matrix)}")  # too low: 1737; too high: 1884


def part_one(tree_matrix: list[list[int]]) -> int:
    visible_trees: int = 0
    end_of_row_index: int = len(tree_matrix) - 1
    end_of_col_index: int = len(tree_matrix[0]) - 1

    for row_index, row_values in enumerate(
        tree_matrix
    ):  # [[3, 0, 3, 7, 3],[2, 5, 5, 1, 2],...]
        for value_index, value in enumerate(row_values):  # value [3, 0, 3, 7, 3]
            if (
                row_index == 0
                or row_index == end_of_row_index
                or value_index == 0
                or value_index == end_of_col_index
                or i_can_see_the_tree(
                    tree_matrix,
                    row_index,
                    end_of_row_index,
                    value,
                    value_index,
                    end_of_col_index,
                )
            ):
                visible_trees += 1
    return visible_trees


def i_can_see_the_tree(
    tree_matrix: list[list[int]],
    row_index: int,
    end_of_row_index: int,
    value: int,
    value_index: int,
    end_of_col_index: int,
) -> bool:

    upper_rows = list(range(0, row_index))  # up
    lower_rows = list(range(row_index + 1, end_of_row_index + 1))  # down

    if all([vals < value for vals in tree_matrix[row_index][:value_index]]):  # left
        return True
    elif all(
        [vals < value for vals in tree_matrix[row_index][value_index + 1 :]]
    ):  # right
        return True
    elif all([tree_matrix[row][value_index] < value for row in upper_rows]):
        return True
    elif all([tree_matrix[row][value_index] < value for row in lower_rows]):
        return True
    else:
        return False


if __name__ == "__main__":
    main()
