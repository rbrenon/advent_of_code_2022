import math
from tqdm import tqdm

def main():
    with open("input.txt") as file:
        raw_input = file.read().splitlines()

    monkeys = create_monkeys(raw_input)
    part_one(monkeys)   # answer: 90882
    monkeys = create_monkeys(raw_input)
    part_two(monkeys)   # answer: 30893109657


def part_one(monkeys: list[dict]) -> None:
    """[{'Monkey 0': {'false_throw': 3,
    'items': [79, 98],
    'operand_a': 'old',
    'operand_b': 19,
    'operation': '*',
    'test_divisor': 23,
    'true_throw': 2}},"""

    for round_no in tqdm(range(1, 21)):
        for index, monkey in enumerate(monkeys):
            for key in monkeys[index].keys():
                for item in monkeys[index][key]["items"]:
                    new_worry_level = calc_worry_score(
                        item,
                        monkeys[index][key]["operand_a"],
                        monkeys[index][key]["operand_b"],
                        monkeys[index][key]["operation"],
                    )
                    new_worry_level = floor_divide(new_worry_level, 3)
                    if mod_divide(new_worry_level, monkeys[index][key]["test_divisor"]):
                        target_monkey = monkeys[index][key]["true_throw"]
                    else:
                        target_monkey = monkeys[index][key]["false_throw"]
                    monkeys[target_monkey][f"Monkey {target_monkey}"]["items"].append(
                        new_worry_level
                    )
                    monkeys[index][key]["inspections"] += 1
                monkeys[index][key]["items"] = []

    monkey_business = list()
    for index, monkey in enumerate(monkeys):
        for key in monkeys[index].keys():
            monkey_business.append(monkeys[index][key]["inspections"])
    print(
        f"Part one: total monkey business = "
        f"{multipy(sorted(monkey_business, reverse=True)[0], sorted(monkey_business, reverse=True)[1])}"
    )


def part_two(monkeys: list[dict]) -> None:
    """[{'Monkey 0': {'false_throw': 3,
    'items': [79, 98],
    'operand_a': 'old',
    'operand_b': 19,
    'operation': '*',
    'test_divisor': 23,
    'true_throw': 2}},"""

    monkey_divisors = list()
    for index, monkey in enumerate(monkeys):
        for key in monkeys[index].keys():
            monkey_divisors.append(monkeys[index][key]["test_divisor"])
    monkey_divisors_lcm = math.lcm(*monkey_divisors)

    for round_no in tqdm(range(1, 10_001)):
        for index, monkey in enumerate(monkeys):
            for key in monkeys[index].keys():
                for item in monkeys[index][key]["items"]:
                    monkeys[index][key]["inspections"] += 1
                    new_worry_level = calc_worry_score(
                        item,
                        monkeys[index][key]["operand_a"],
                        monkeys[index][key]["operand_b"],
                        monkeys[index][key]["operation"],
                    )
                    new_worry_level %= monkey_divisors_lcm
                    if new_worry_level % monkeys[index][key]["test_divisor"] == 0:
                        target_monkey = monkeys[index][key]["true_throw"]
                    else:
                        target_monkey = monkeys[index][key]["false_throw"]
                    monkeys[target_monkey][f"Monkey {target_monkey}"]["items"].append(
                        new_worry_level
                    )

                monkeys[index][key]["items"] = []

    monkey_business = list()
    for index, monkey in enumerate(monkeys):
        for key in monkeys[index].keys():
            monkey_business.append(monkeys[index][key]["inspections"])
    print(
        f"Part two: total monkey business = "
        f"{multipy(sorted(monkey_business, reverse=True)[0], sorted(monkey_business, reverse=True)[1])}"
    )


def calc_worry_score(item: int, op_a: str, op_b: str, operation: str) -> int:
    if op_a == "old":
        op_a = item
    if op_b == "old":
        op_b = item

    if operation == "+":
        worry_score = add(op_a, op_b)
    elif operation == "-":
        worry_score = subtract(op_a, op_b)
    elif operation == "*":
        worry_score = multipy(op_a, op_b)
    elif operation == "/":
        worry_score = floor_divide(op_a, op_b)

    return worry_score


def add(a: int, b: int) -> int:
    return a + b


def subtract(a: int, b: int) -> int:
    return a - b


def multipy(a: int, b: int) -> int:
    return a * b


def floor_divide(a: int, b: int) -> int:
    return a // b


def mod_divide(a: int, b: int) -> bool:
    return True if a % b == 0 else False


def create_monkeys(data: list[str]) -> list[dict]:
    monkeys = list()
    for item in data:
        if item.startswith("Monkey"):
            monkey_name = item[:-1]
        elif item.strip().startswith("Starting"):
            split_items = item.replace(":", ",").strip().split(",")
            monkey_items = list()
            for split_item in split_items:
                try:
                    monkey_items.append(int(split_item))
                except Exception as e:
                    ...
        elif item.strip().startswith("Operation"):
            split_item = item.split(" ")
            monkey_operation = split_item[-2]
            monkey_operand_a = split_item[-3]
            try:
                monkey_operand_b = int(split_item[-1])
            except Exception as e:
                monkey_operand_b = split_item[-1]
        elif item.strip().startswith("Test"):
            monkey_test_divisor = int(item.split(" ")[-1])
        elif item.strip().startswith("If true"):
            monkey_true_throw = int(item.split(" ")[-1])
        elif item.strip().startswith("If false"):
            monkey_false_throw = int(item.split(" ")[-1])
            monkey = {
                monkey_name: {
                    "items": monkey_items,
                    "operand_a": monkey_operand_a,
                    "operation": monkey_operation,
                    "operand_b": monkey_operand_b,
                    "test_divisor": monkey_test_divisor,
                    "true_throw": monkey_true_throw,
                    "false_throw": monkey_false_throw,
                    "inspections": 0,
                }
            }
            monkeys.append(monkey)

    """{'Monkey 0': {
                  'false_throw': 3,
                  'items': [79, 98],
                  'operand_a': 'old',
                  'operand_b': 19,
                  'operation': '*',
                  'test_divisor': 23,
                  'true_throw': 2}}
    """

    return monkeys


if __name__ == "__main__":
    main()
