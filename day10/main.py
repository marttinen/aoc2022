import os

def part1(input: str) -> int:
    signals = []
    cycle = 0
    regx = 1

    def tick():
        nonlocal cycle
        cycle += 1
        if (cycle + 20) % 40 == 0:
            signals.append(cycle * regx)

    for command in input.splitlines():
        match command.split(' '):
            case ['noop']:
                tick()

            case ['addx', x]:
                tick()
                tick()
                regx += int(x)

    return sum(signals)

def part2(input: str) -> str:
    cycle = 0
    regx = 1
    crt = ''

    def tick():
        nonlocal cycle, crt
        cycle += 1

        if cycle % 40 == 0:
            crt += '\n'
        elif cycle % 40 in [regx-1, regx, regx+1]:
            crt += '#'
        else:
            crt += '.'

    for command in input.splitlines():
        match command.split(' '):
            case ['noop']:
                tick()

            case ['addx', x]:
                tick()
                regx += int(x)
                tick()

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
