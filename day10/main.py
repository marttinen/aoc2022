import os

def part1(input: str) -> int:
    cycle = 1
    regx = 1
    signals = []

    def tick():
        nonlocal cycle, signals
        if (cycle + 20) % 40 == 0:
            signals.append(cycle * regx)
        cycle += 1

    for command in input.splitlines():
        if command == 'noop':
            tick()
        elif command[0:4] == 'addx':
            tick()
            tick()
            regx += int(command[len('addx'):])
        else:
            print(f'unknown command {command}')

    return sum(signals)

def part2(input: str) -> str:
    cycle = 1
    regx = 1
    crt = ''

    def tick():
        nonlocal cycle, crt

        if (cycle-1) % 40 in [regx-1, regx, regx+1]:
            crt += '#'
        else:
            crt += '.'
        if cycle % 40 == 0:
            crt += '\n'

        cycle += 1

    for command in input.splitlines():
        if command == 'noop':
            tick()
        elif command[0:4] == 'addx':
            tick()
            tick()
            regx += int(command[len('addx'):])
        else:
            print(f'unknown command {command}')

    return crt

if __name__ == '__main__':
    dir = os.path.dirname(__file__)
    for filename in ['test.txt', 'input.txt']:
        if os.path.exists(f'{dir}/{filename}'):
            with open(f'{dir}/{filename}') as f:
                input = f.read()
            print(f'== {filename} ==')
            print(part1(input))
            print(part2(input))
