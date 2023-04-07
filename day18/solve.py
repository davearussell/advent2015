#! /usr/bin/python3
import sys


def parse_input(path):
    lines = open(path).read().strip().split('\n')
    grid = set()
    for y, row in enumerate(lines):
        for x, cell in enumerate(row):
            if cell == '#':
                grid.add((x, y))
    return grid


def iterate(grid, n, part2=False):
    for _ in range(n):
        new_grid = set()
        if part2:
            new_grid = {(0, 0), (99, 0), (0, 99), (99, 99)}
        for x in range(100):
            for y in range(100):
                on = (x, y) in grid
                neighbours = {(x - 1, y - 1), (x, y - 1), (x + 1, y - 1),
                              (x - 1, y), (x + 1, y),
                              (x - 1, y + 1), (x, y + 1), (x + 1, y + 1)}
                n = len(neighbours & grid)
                if n == 3 or (on and n == 2):
                    new_grid.add((x, y))
        grid = new_grid
    return len(grid)


def main(input_file):
    grid = parse_input(input_file)
    print("Part 1:", iterate(grid, 100, False))
    print("Part 2:", iterate(grid, 100, True))


if __name__ == '__main__':
    main(sys.argv[1])
