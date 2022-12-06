from dataclasses import dataclass


@dataclass
class CrateStack:
    crates: list

    def move(self, destination, amount):
        for i in range(0, amount):
            item = self.crates.pop(0)
            print(f"{item=}")
            destination.crates.insert(0, item)

    def move_9001(self, destination, amount):
        crates_to_move = self.crates[:amount]
        self.crates = self.crates[amount:]
        destination.crates = crates_to_move + destination.crates


def input_data(path: str):
    with open(path) as f:
        return f.read().splitlines()


def execute_rule(rule: str, stacks: dict):
    amount, origin, destination = [int(s) for s in rule.split() if s.isdigit()]
    origin = stacks[origin]
    destination = stacks[destination]

    origin.move(destination, amount)


def execute_rule_d2(rule: str, stacks: dict):
    amount, origin, destination = [int(s) for s in rule.split() if s.isdigit()]
    origin = stacks[origin]
    destination = stacks[destination]

    origin.move_9001(destination, amount)


def process_data(data):
    space_between_letters = 4
    start_index = 1

    stacks = {}
    moves = []

    for line in data:
        if line.startswith("m"):
            moves.append(line)

        elif "[" in line:
            for stack_index, index in enumerate(range(start_index, len(line), space_between_letters)):
                letter = line[index]
                if letter.isalpha():
                    stacks.setdefault(stack_index, [])
                    stacks[stack_index].append(letter)

    stacks = {key+1: CrateStack(value) for key, value in stacks.items()}

    return stacks, moves


if __name__ == "__main__":
    data = input_data("data/input.txt")
    stacks, rules = process_data(data)
    print(f"{stacks=}")
    print(f"{rules=}")

    # day 1
    for rule in rules:
        execute_rule(rule, stacks)
        print(stacks)

    for index, stack in stacks.items():
        print(f"{index}: {stack.crates[0]}")

    # day 2
    for rule in rules:
        execute_rule_d2(rule, stacks)
        print(stacks)

    for index, stack in stacks.items():
        print(f"{index}: {stack.crates[0]}")