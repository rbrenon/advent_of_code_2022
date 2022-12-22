class Coord:
    def __init__(self, x=0, y=0, stepped=False):
        self.x = x
        self.y = y
        self.coords_visited = [(self.x, self.y)]

    def __str__(self):
        return f"({self.x},{self.y})"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return True if self.x == other.x and self.y == other.y else False

    def move(self, direction):
        self.x = self.x + direction.x
        self.y = self.y + direction.y

    def move_to_location(self, coordinates):
        self.x = coordinates[0]
        self.y = coordinates[1]

    def needs_to_move(self, target) -> bool:
        if self == target:
            return False
        else:
            for direction in ["UR", "DR", "R", "UL", "DL", "L", "U", "D"]:
                neighbor_coord = Coord(target.x, target.y)
                neighbor_coord.move(DIRECTION_DICT[direction])
                if self == neighbor_coord:
                    return False
        return True

    def determine_move_direction(self, head) -> str:
        if head.x >= self.x + 2:  # right
            if head.y > self.y:  # 2,1 - 0,0 --> 2,1 - 1,1
                return "UR"
            elif head.y < self.y:  # 2,1 - 0,2 --> 2,1 - 1,1
                return "DR"
            else:  # 2,0 -- 0,0 --> 2,0 - 1,0
                return "R"
        elif head.x <= self.x - 2:  # left
            if head.y > self.y:  # 0,1 - 2,0 --> 0,1 - 1,1
                return "UL"
            elif head.y < self.y:  # 0,0 - 2,1 --> 0,0 - 1,0
                return "DL"
            else:  # 0,0 - 2,0 --> 0,0 - 1,0
                return "L"
        elif head.y >= self.y + 2:  # up
            if head.x > self.x:  # 1,2 - 0,0 --> 1,2 - 1,1
                return "UR"
            elif head.x < self.x:  # -1,2 - 0,0 --> -1,2 - -1,1
                return "UL"
            else:  # 0,2 - 0,0 --> 0,2 - 0,1
                return "U"
        elif head.y <= self.y - 2:  # down
            if head.x > self.x:
                return "DR"
            elif head.x < self.x:
                return "DL"
            else:  # h: 0,0 -- 0,2 :t
                return "D"


DIRECTION_DICT = {
    "R": Coord(1, 0),
    "L": Coord(-1, 0),
    "U": Coord(0, 1),
    "D": Coord(0, -1),
    "UR": Coord(1, 1),
    "DR": Coord(1, -1),
    "DL": Coord(-1, -1),
    "UL": Coord(-1, 1),
}


def part_one(input_instructions: list[str]) -> None:
    head = Coord(0, 0)
    tail = Coord(0, 0)

    for step in input_instructions:
        direction, distance = step.split(" ")  # 'R', '4'
        for each_step in range(0, int(distance)):  # iterate 0->4
            head.move(DIRECTION_DICT[direction])
            if tail.needs_to_move(head):
                tail.move(DIRECTION_DICT[tail.determine_move_direction(head)])
                tail.coords_visited.append((tail.x, tail.y))

    tail_coords_visited = set(tail.coords_visited)
    print(f"Part one: {len(tail_coords_visited)}")    # answer: 5710


def part_two(input_instructions: list[str]) -> None:
    rope = {
        "head": Coord(0, 0),
        "k1": Coord(0, 0),
        "k2": Coord(0, 0),
        "k3": Coord(0, 0),
        "k4": Coord(0, 0),
        "k5": Coord(0, 0),
        "k6": Coord(0, 0),
        "k7": Coord(0, 0),
        "k8": Coord(0, 0),
        "k9": Coord(0, 0)
    }

    for step in input_instructions:
        direction, distance = step.split(" ")  # 'R', '4'
        for each_step in range(0, int(distance)):  # iterate 0->4
            rope["head"].move(DIRECTION_DICT[direction])
            for key in rope.keys():
                if key != "head":
                    if rope[key].needs_to_move(rope[previous_rope_key]):
                        rope[key].move(DIRECTION_DICT[rope[key].determine_move_direction(rope[previous_rope_key])])
                        rope[key].coords_visited.append((rope[key].x, rope[key].y))
                previous_rope_key = key

    tail_coords_visited = set(rope['k9'].coords_visited)
    print(f"Part two: {len(tail_coords_visited)}")    # answer: 2259; too high: 4477


def main():
    with open("input.txt") as file:
        file_input = file.read().splitlines()  # ['R 4', 'U 4',...]

    part_one(file_input)
    part_two(file_input)


if __name__ == "__main__":
    main()
