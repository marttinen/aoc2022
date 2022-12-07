import os
import vfs

def part1(input: str) -> int:
    root = vfs.build_vfs(input)
    sizes = root.size_list([])

    return sum([s for s in sizes if s<100000])

def part2(input: str) -> int:
    root = vfs.build_vfs(input)
    unused_space = 70_000_000 - root.size()
    required_space = 30_000_000 - unused_space

    print(f'unused_space:   {unused_space}')
    print(f'required_space: {required_space}')

    sizes = root.size_list([])
    smallest = root.size()
    for s in sizes:
        if s > required_space and s < smallest:
            smallest = s

    return smallest

if __name__ == '__main__':
    dir = os.path.dirname(__file__)
    for filename in ['test.txt', 'input.txt']:
        if os.path.exists(f'{dir}/{filename}'):
            with open(f'{dir}/{filename}') as f:
                input = f.read()
            print(f'== {filename} ==')
            print(part1(input))
            print(part2(input))

