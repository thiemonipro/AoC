import time
from dataclasses import dataclass

from functools import cache


def input_data(path: str):
    with open(path) as f:
        return f.read().splitlines()


@dataclass
class Grid:
    board: list
    width: int
    height: int

    def __init__(self, board, width, height):
        self.board = [int(item) for sublist in board for item in sublist]
        self.width = width
        self.height = height

    @cache
    def get_row(self, index):
        return self.board[index * self.width: index * self.width + self.width]

    @cache
    def get_column(self, index):
        return [self.board[i * self.height + index] for i in range(self.height)]


    def value_by_index(self, x, y):
        val_index = y * self.height + x
        return self.board[val_index]

    def is_visible(self, x, y):
        tree_val = self.value_by_index(x, y)

        row = self.get_row(y)
        column = self.get_column(x)

        # should this be changed to generators we iterate over?
        # slicing the whole list now while we might only need a very small part of the data
        # could split it off in a separate function that checks if there are obstacles in that way
        left = row[:x]
        right = row[x + 1:]
        up = column[:y]
        down = column[y + 1:]

        for arr in left, right, up, down:
            for item in arr:
                if item >= tree_val:
                    break
            else:
                return True

        return False

    def score_tree(self, x, y):
        tree_val = self.value_by_index(x, y)

        # slice left, right, up and down
        row = self.get_row(y)
        column = self.get_column(x)

        left = row[:x]
        right = row[x + 1:]
        up = column[:y]
        down = column[y + 1:]

        score = 1
        for direction in [reversed(left), right, reversed(up), down]:
            view_distance = self.calculate_view_distance(tree_val, direction)
            score *= view_distance
        return score

    def calculate_view_distance(self, height, neighbours):
        counter = 0
        for tree in neighbours:
            if tree < height:
                counter += 1
            else:
                counter += 1
                break

        return counter

    def visible_trees(self):
        counter = 0
        for x in range(self.width):
            for y in range(self.height):
                # trees on edges
                if x == 0 or x == self.width - 1 or y == 0 or y == self.height - 1:
                    counter += 1
                    continue

                if self.is_visible(x, y):
                    counter += 1
                    # print(f"center tree: {x, y} is visible with value: {self.value_by_index(x, y)}")

        return counter

    def most_scenic_tree(self):
        highest_score = 0
        for x in range(self.width):
            for y in range(self.height):
                if x == 0 or x == self.width - 1 or y == 0 or y == self.height - 1:
                    continue

                score = self.score_tree(x, y)
                if highest_score < score:
                    highest_score = score
        return highest_score

    def pretty_print(self):
        print(f"{self.width=}")
        print(f"{self.height=}")
        for i in range(self.height):
            print(self.get_row(i))

    def __hash__(self):
        return 1


if __name__ == "__main__":
    data = input_data("data/2000x2000.txt")
    grid = Grid(board=data, width=len(data[0]), height=len(data))
    grid.pretty_print()
    print(f"*" * 120)

    # part 1
    start = time.time()
    print(grid.visible_trees())
    end = time.time()
    print(f"p1 took: {end-start} s")

    # part 2
    start = time.time()
    tree = grid.most_scenic_tree()
    print(f"top tree: {tree}")
    end = time.time()
    print(f"p2 took: {end - start} s")