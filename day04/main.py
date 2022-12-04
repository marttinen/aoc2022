import sys

def part1(input: str) -> int:
    overlap = 0
    for elve_tasks in input.splitlines():
        ab, cd = elve_tasks.split(',')
        [a, b], [c, d] = ab.split('-'), cd.split('-')
        a, b, c, d = int(a), int(b), int(c), int(d)

        if a <= c <= d <= b or c <= a <= b <= d:
            overlap += 1

    return overlap

def part2(input: str) -> int:
    overlap = 0
    for elve_tasks in input.splitlines():
        ab, cd = elve_tasks.split(',')
        [a, b], [c, d] = ab.split('-'), cd.split('-')
        a, b, c, d = int(a), int(b), int(c), int(d)

        if a <= c <= d <= b or c <= a <= b <= d:
            overlap += 1
        elif a <= c and c <= b <= d:
            overlap += 1
        elif b >= d and d >= a >= c:
            overlap += 1

    return overlap

if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        input = f.read()
        print(part1(input))
        print(part2(input))
