import os

def part1(input: str) -> int:
    signals = []
    cycle = 0
    reg_x = 1

    def tick(cycle):
        cycle += 1
        if (cycle + 20) % 40 == 0:
            signals.append(cycle * reg_x)
            print(f'cycle {cycle}, X {reg_x}, signals {signals}')
        return cycle

    for command in input.splitlines():
        match command.split(' '):
            case ['noop']:
                cycle = tick(cycle)

            case ['addx', x]:
                cycle = tick(cycle)
                cycle = tick(cycle)
                reg_x += int(x)

    return sum(signals)

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
