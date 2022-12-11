import math
import os
import monkey

def part1(input: str) -> int:
    monkeys: list[monkey.Monkey] = [monkey.parse_monkey(i) for i in input.split('\n\n')]

    rounds = 20
    for _ in range(rounds):
        for m in monkeys:
            m.inspect(monkeys)

    for m in monkeys:
        print(m)

    business = sorted([m.monkey_business for m in monkeys])
    return math.prod(business[-2:])

def part2(input: str) -> int:
    return 0

if __name__ == '__main__':
    dir = os.path.dirname(__file__)
    for filename in ['test.txt', 'input.txt']:
        if os.path.exists(f'{dir}/{filename}'):
            with open(f'{dir}/{filename}') as f:
                input = f.read()
            print(f'== {filename} ==')
            print(part1(input))
            print(part2(input))
