# Advent of Code 2022

The solutions are written in a "good enough to get the job done" code style with Python 3.

## Minimal runner setup

Every `dayXY` folder will have a main.py with the same basic setup

```py
import sys

def part1(input: str) -> int:
    ...

def part2(input: str) -> int:
    ...

if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        input = f.read()
        print(part1(input))
        print(part2(input))
```
