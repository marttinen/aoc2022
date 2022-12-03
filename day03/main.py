import sys

def priorities(items: list[str]) -> int:
    priorities = 0
    for item in items:
        if item.islower():
            priorities += ord(item) - ord('a') + 1
        else:
            priorities += ord(item) - ord('A') + 27
    return priorities

def part1(input: str) -> int:
    shared_items = []
    for rucksack in input.splitlines():
        bag1 = rucksack[:len(rucksack)//2]
        bag2 = rucksack[len(rucksack)//2:]
        shared_items.extend(set(bag1).intersection(bag2))
    return priorities(shared_items)

def part2(input: str) -> int:
    return 0

if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        input = f.read()
        print(part1(input))
        print(part2(input))
