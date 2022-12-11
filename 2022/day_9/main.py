from dataclasses import dataclass

# value = index, movement multiplier
movement_dict = {"L": (0, -1), "R": (0, 1), "U": (1, 1), "D": (1, -1)}


@dataclass
class Rope:
    head: list
    tail: list
    tail_moves: set
    knot: int

    def is_touching(self):
        dif_x = abs(self.head[0] - self.tail[0])
        dif_y = abs(self.head[1] - self.tail[1])
        # print(f"{dif_x=}")
        # print(f"{dif_y=}")
        return not (dif_x > 1 or dif_y > 1)

    def move(self, command):
        direction, amount = command.split(" ")
        index, movement_multiplier = movement_dict[direction]
        for i in range(int(amount)):
            self.head[index] += movement_multiplier
            print(f"{direction}: {i}")
            self.sync_tail()
            self.move_knot()

    def move_tail(self):
        x_movement_modifier = -1 if self.tail[0] > self.head[0] else 1
        y_movement_modifier = -1 if self.tail[1] > self.head[1] else 1

        if self.tail[0] == self.head[0]:
            #print(f"moving height")
            self.tail[1] += y_movement_modifier
        elif self.tail[1] == self.head[1]:
            #print(f"moving width")
            self.tail[0] += x_movement_modifier
        else:
            #print(f"moving diagonally")
            self.tail[1] += y_movement_modifier
            self.tail[0] += x_movement_modifier

        #print(f"moved to: {self.tail}")
        self.tail_moves.add(tuple(self.tail))

    def sync_tail(self):
        if not self.is_touching():
            self.move_tail()

    def move_knot(self):
        if self.knot:
            #print(f"moving knot")
            self.knot.head = self.tail
            self.knot.sync_tail()
            self.knot.move_knot()


def input_data(path: str):
    with open(path) as f:
        return f.read().splitlines()


if __name__ == "__main__":
    moves = input_data("data/input.txt")
    rope = Rope([0, 0], [0, 0], set([]), None)

    for move in moves:
        rope.move(move)

    # part 1
    print(rope.tail_moves)
    print(f"part 1: {len(rope.tail_moves) + 1}")  # add 1 to add the starting value.....

    # part 2
    ropes = [Rope([0, 0], [0, 0], set([]), None)]
    prev_rope = ropes[0]

    for i in range(9):
        new_rope = Rope([0, 0], [0, 0], set([]), None)
        ropes.append(new_rope)
        prev_rope.knot = new_rope
        prev_rope = new_rope

    print(f"part 2 using {len(ropes)} ropes")

    head_rope = ropes[0]

    for step, move in enumerate(moves):
        print(f"{step=}")
        head_rope.move(move)

    last_knot = ropes[-2]
    print(f"{last_knot=}")
    print(f"part 2: {len(last_knot.tail_moves) + 1}")
