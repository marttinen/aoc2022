import sys

def calories(input: str) -> list[int]:
    calories: list[int] = [0]
    for cal in input.splitlines():
        if cal == "":
            calories.append(0)
        else:
            last = calories.pop()
            last += int(cal)
            calories.append(last)
    return calories

def part1(input: str) -> str:
    cals = calories(input)    
    return max(cals)

def part2(input: str) -> str:
    cals = calories(input)
    return sum(sorted(cals)[-3:])

if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        input = f.read()
        print(part1(input))
        print(part2(input))
