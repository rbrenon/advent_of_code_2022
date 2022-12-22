class Coord:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.coords_visited = {(self.x, self.y)}

    def __str__(self):
        return f"({self.x},{self.y})"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return True if self.x == other.x and self.y == other.y else False

    def move(self, direction):
        self.x = self.x + direction.x
        self.y = self.y + direction.y

    def needs_to_move(self, head, tail) -> bool:
        if head == tail:
            return False
        else:
            for direction in ["UR", "DR", "R", "UL", "DL", "L", "U", "D"]:
                neighbor_coord = Coord(head.x, head.y)
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
        else:
            print(f"no direction returned")
        return None


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


def part_one(input_instructions: list[str], head: Coord, tail: Coord) -> None:
    dirs_moved = list()
    for step in input_instructions:
        direction, distance = step.split(" ")  # 'R', '4'
        for each_step in range(0, int(distance)):  # iterate 0->4
            head.move(DIRECTION_DICT[direction])
            if tail.needs_to_move(head, tail):
                tail_direction = tail.determine_move_direction(head)
                dirs_moved.append(tail_direction)
                tail.move(DIRECTION_DICT[tail_direction])
                tail.coords_visited.add((tail.x, tail.y))

    print(f"Part one: {len(tail.coords_visited)}")    # answer: 5710


def main():
    with open("input.txt") as file:
        file_input = file.read().splitlines()  # ['R 4', 'U 4',...]

    head = Coord(0, 0)
    tail = Coord(0, 0)

    part_one(file_input, head, tail)


if __name__ == "__main__":
    main()
