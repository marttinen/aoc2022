import sys

SCORE_DRAW = 3
SCORE_WIN = 6

def rock_paper_scissors_part1(game: str) -> int:
    opponent, player = game.split(' ')
    player_choice = ord(player) - ord('X')
    opponent_choice = ord(opponent) - ord('A')
    player_score = player_choice + 1
    if player_choice == ((opponent_choice + 1) % 3):
        return player_score + SCORE_WIN
    elif opponent_choice == player_choice:
        return player_score + SCORE_DRAW
    else:
        return player_score

def rock_paper_scissors_part2(game: str) -> int:
    move, end = game.split(' ')
    score = ord(move) - ord('A') + 1
    match [move, end]:
        case [_, 'X']: return (score - 1 if score > 1 else 3)
        case [_, 'Y']: return SCORE_DRAW + score
        case [_, 'Z']: return SCORE_WIN + (score + 1 if score < 3 else 1)

def part1(input: str) -> int:
    score = 0
    for game in input.splitlines():
        score += rock_paper_scissors_part1(game)
    return score

def part2(input: str) -> int:
    score = 0
    for game in input.splitlines():
        score += rock_paper_scissors_part2(game)
    return score

if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        input = f.read()
        print(part1(input))
        print(part2(input))
