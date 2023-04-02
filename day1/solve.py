#! /usr/bin/python3
import sys


def main(input_file):
    brackets = open(input_file).read().strip()
    floors = [0]
    for char in brackets:
        floors.append(floors[-1] + (1 if char == '(' else -1))
    print("Part 1:", floors[-1])
    print("Part 2:", floors.index(-1))


if __name__ == '__main__':
    main(sys.argv[1])
