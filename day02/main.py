import sys

SCORE_DRAW = 3
SCORE_WIN = 6

def rps1(opponent: str, player: str) -> int:
    opponent_choice = ord(opponent) - ord('A')
    player_choice = ord(player) - ord('X')

    if player_choice == (opponent_choice + 1) % 3:
        return player_choice + 1 + SCORE_WIN
    elif opponent_choice == player_choice:
        return player_choice + 1 + SCORE_DRAW
    else:
        return player_choice + 1

def rps2(move: str, outcome: str) -> int:
    score = ord(move) - ord('A') + 1
    match [move, outcome]:
        case [_, 'X']: return (score - 1 if score > 1 else 3)
        case [_, 'Y']: return SCORE_DRAW + score
        case [_, 'Z']: return SCORE_WIN + (score + 1 if score < 3 else 1)

def part1(input: str) -> int:
    score = 0
    for game in input.splitlines():
        a, b = game.split(' ')
        score += rps1(a, b)
    return score

def part2(input: str) -> int:
    score = 0
    for game in input.splitlines():
        a, b = game.split(' ')
        score += rps2(a, b)
    return score

if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        input = f.read()
        print(part1(input))
        print(part2(input))
