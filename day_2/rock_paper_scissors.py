

def main():
    with open("input.txt") as file:
        draws = file.read().splitlines()

    part_one(draws)
    part_two(draws)


def part_one(draws: list[str]) -> None:

    rps = {
        'elf_winners': [
            ['A', 'Z'],
            ['B', 'X'],
            ['C', 'Y']],
        'human_winners': [
            ['A', 'Y'],
            ['B', 'Z'],
            ['C', 'X']],
        'elf_score': 0,
        'human_score': 0,
        'A': {
            'object': 'Rock',
            'points': 1
        },
        'B': {
            'object': 'Paper',
            'points': 2
        },
        'C': {
            'object': 'Scissors',
            'points': 3
        },
        'X': {
            'object': 'Rock',
            'points': 1
        },
        'Y': {
            'object': 'Paper',
            'points': 2
        },
        'Z': {
            'object': 'Scissors',
            'points': 3
        },
    }

    for draw in draws:
        elf_play, human_play = draw.split(' ')
        if [elf_play, human_play] in rps['elf_winners']:
            rps['elf_score'] += 6 + rps[elf_play]['points']
            rps['human_score'] += rps[human_play]['points']
        elif [elf_play, human_play] in rps['human_winners']:
            rps['elf_score'] += rps[elf_play]['points']
            rps['human_score'] += 6 + rps[human_play]['points']
        else:
            rps['elf_score'] += 3 + rps[elf_play]['points']
            rps['human_score'] += 3 + rps[human_play]['points']

    print(f"Part One: Elf = {rps['elf_score']} Human = {rps['human_score']}")   # human 12586
    return


def part_two(draws: list[str]) -> None:
    rps = {
        'human_result': {
            'X': 'elf_winners',
            'Y': 'draw',
            'Z': 'human_winners'
        },
        'elf_winners': [
            ['A', 'Z'],
            ['B', 'X'],
            ['C', 'Y']],
        'human_winners': [
            ['A', 'Y'],
            ['B', 'Z'],
            ['C', 'X']],
        'elf_score': 0,
        'human_score': 0,
        'A': {
            'object': 'Rock',
            'points': 1
        },
        'B': {
            'object': 'Paper',
            'points': 2
        },
        'C': {
            'object': 'Scissors',
            'points': 3
        },
        'X': {
            'object': 'Rock',
            'points': 1
        },
        'Y': {
            'object': 'Paper',
            'points': 2
        },
        'Z': {
            'object': 'Scissors',
            'points': 3
        },
    }

    for draw in draws:
        elf_play, human_result = draw.split(' ')
        if human_result == 'X':  # human lose
            for elf_wins in rps['elf_winners']:
                if elf_play in elf_wins:
                    human_play = elf_wins[1]
                    break
            rps['elf_score'] += 6 + rps[elf_play]['points']
            rps['human_score'] += rps[human_play]['points']
        elif human_result == 'Z':  # human win
            for human_win in rps['human_winners']:
                if elf_play in human_win:
                    human_play = human_win[1]
                    break
            rps['elf_score'] += rps[elf_play]['points']
            rps['human_score'] += 6 + rps[human_play]['points']
        else:  # tie
            rps['elf_score'] += 3 + rps[elf_play]['points']
            rps['human_score'] += 3 + rps[elf_play]['points']

    print(f"Part Two: Elf = {rps['elf_score']} Human = {rps['human_score']}")  # human 13193
    return


if __name__ == "__main__":
    main()
