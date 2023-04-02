#! /usr/bin/python3
import sys


def parse_input(path):
    shapes = []
    for line in open(path).read().strip().split('\n'):
        a, b, c = map(int, line.split('x'))
        shapes.append((a, b, c))
    return shapes


def required_paper(shape):
    a, b, c = sorted(shape)
    return (3 * a * b) + (2 * a * c) + (2 * b * c)


def required_ribbon(shape):
    a, b, c = sorted(shape)
    return 2 * (a + b) + a * b * c


def main(input_file):
    shapes = parse_input(input_file)
    print("Part 1:", sum(map(required_paper, shapes)))
    print("Part 2:", sum(map(required_ribbon, shapes)))


if __name__ == '__main__':
    main(sys.argv[1])
