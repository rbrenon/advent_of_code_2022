

def main():
    with open("input.txt") as file:
        raw_input = file.read().splitlines()

    part_one(raw_input)


def part_one(instructions: list[str]) -> None:
    index: int = 1
    signal_strength = dict()
    signal_value = 1
    sprites = list()

    for _, signal in enumerate(instructions, start=1):
        if signal.startswith('noop'):
            sprites.append(check_sprite(index, signal_value))
            index += 1
            signal_strength[index] = signal_value
        else:
            strength: int = int(signal.split()[1])
            for i in [1]:
                sprites.append(check_sprite(index, signal_value))
                index += 1
                signal_strength[index] = signal_value
            signal_value += strength
            sprites.append(check_sprite(index, signal_value))
            index += 1
            signal_strength[index] = signal_value

    print(f"Part one: {calc_signal_strength(signal_strength)}")     # 13720

    print("Part two:")
    for sprite_index, pixel in enumerate(sprites, start=1):
        if pixel:
            print('*', end='')
        else:
            print(' ', end='')
        if sprite_index % 40 == 0 and sprite_index > 0:
            print()
    # FBURHZCH


def check_sprite(index: int, signal_value: int) -> bool:
    index %= 40
    signal_value = abs(signal_value)
    signal_value %= 40
    return signal_value - 1 <= index <= signal_value + 1


def calc_signal_strength(signal_strength: dict) -> int:
    sum_of_signal_strength: int = 0
    for signal in [20, 60, 100, 140, 180, 220]:
        sum_of_signal_strength += (signal_strength[signal] * signal)

    return sum_of_signal_strength


if __name__ == "__main__":
    main()