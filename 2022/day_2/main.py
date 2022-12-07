from enum import Enum

class RoundOutcome(Enum):
    WIN = 6
    DRAW = 3
    LOST = 0


class Shapes(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


opponent_moves = {"A": Shapes.ROCK, "B": Shapes.PAPER, "C": Shapes.SCISSORS}
player_moves = {"X": Shapes.ROCK, "Y": Shapes.PAPER, "Z": Shapes.SCISSORS}

scores = {"A": 1, "B": 2, "C": 3}

expected_outcome = {"Z": RoundOutcome.WIN ,"Y": RoundOutcome.DRAW, "X": RoundOutcome.LOST}

WINNING_MOVES = {Shapes.ROCK: Shapes.SCISSORS, Shapes.PAPER: Shapes.ROCK, Shapes.SCISSORS: Shapes.PAPER}
LOSING_MOVES = {value: key for key, value in WINNING_MOVES.items()}


def input_data(path: str):
    with open(path) as f:
        return f.read().splitlines()


def score_game(rounds):
    scores = [0]
    for round in rounds:
        opponent, player = round.split(" ")
        opponent = opponent_moves[opponent]
        player = player_moves[player]
        scores.append(score_turn(opponent, player))
    return sum(scores)


def score_game_p2(rounds):
    scores = [0]
    for round in rounds:
        opponent, player = round.split(" ")
        opponent = opponent_moves[opponent]
        outcome = expected_outcome[player]
        player = calculate_move(outcome, opponent)
        scores.append(score_turn(opponent, player))
    return sum(scores)


def calculate_move(outcome, opponent_move):
    if outcome == RoundOutcome.DRAW:
        return opponent_move
    elif outcome == RoundOutcome.LOST:
        return WINNING_MOVES[opponent_move]
    else:
        return LOSING_MOVES[opponent_move]


def score_turn(opponent, player) -> int:
    score = 0
    if opponent == player:
        score += RoundOutcome.DRAW.value
    elif WINNING_MOVES[player] == opponent:
        score += RoundOutcome.WIN.value
    else:
        score += RoundOutcome.LOST.value
    score += player.value
    return score


if __name__ == "__main__":
    data = input_data("data/input.txt")

    # part 1
    total_score = score_game(data)
    print(total_score)

    # part 2
    total_score = score_game_p2(data)
    print(total_score)