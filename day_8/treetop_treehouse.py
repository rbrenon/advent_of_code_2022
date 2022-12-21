from math import prod


def main():
    with open("input.txt") as file:
        file_contents = file.read().splitlines()

    tree_matrix = [
        [int(tree) for tree in file_contents[row_index]]
        for row_index, row in enumerate(file_contents)
    ]

    find_the_tree(tree_matrix)
    return


def find_the_tree(tree_matrix: list[list[int]]):
    end_of_row_index: int = len(tree_matrix) - 1
    end_of_col_index: int = len(tree_matrix[0]) - 1
    visible_trees: int = 0
    scene_scores = list()

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
                )
            ):
                visible_trees += 1

            # Part 2
            scene_scores.append(
                calculate_scene_score(
                    tree_matrix,
                    row_index,
                    value_index,
                    value,
                    end_of_row_index,
                    end_of_col_index,
                )
            )

    print(f"Part one: {visible_trees}")  # answer: 1801; too low: 1737; too high: 1884
    print(
        f"Part two: {max(scene_scores)}"
    )  # answer: 209_880; too high: 940_170; too low: 55_440


def calculate_scene_score(
    tree_matrix: list[list[int]],
    row_index: int,
    value_index: int,
    value: int,
    end_of_row_index: int,
    end_of_col_index: int,
) -> int:
    if (
        row_index == 0
        or row_index == end_of_row_index
        or value_index == 0
        or value_index == end_of_col_index
    ):
        return 0

    upper_rows = list(range(row_index - 1, -1, -1))  # up
    lower_rows = list(range(row_index + 1, end_of_row_index + 1))  # down

    scores: list[int] = [0, 0, 0, 0]

    for left_tree in tree_matrix[row_index][value_index - 1 :: -1]:
        if left_tree <= value:
            scores[0] += 1
        if left_tree >= value:
            break
    for right_tree in tree_matrix[row_index][value_index + 1 :]:
        if right_tree <= value:
            scores[1] += 1
        if right_tree >= value:
            break
    for row in upper_rows:
        if tree_matrix[row][value_index] <= value:
            scores[2] += 1
        if tree_matrix[row][value_index] >= value:
            break
    for row in lower_rows:
        if tree_matrix[row][value_index] <= value:
            scores[3] += 1
        if tree_matrix[row][value_index] >= value:
            break
    return prod(scores)


def i_can_see_the_tree(
    tree_matrix: list[list[int]],
    row_index: int,
    end_of_row_index: int,
    value: int,
    value_index: int,
) -> bool:

    upper_rows = list(range(row_index - 1, -1, -1))  # up
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
