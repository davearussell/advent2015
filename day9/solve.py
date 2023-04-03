#! /usr/bin/python3
import itertools
import sys


def parse_input(path):
    distances = {}
    for line in open(path).read().strip().split('\n'):
        spl = line.split()
        src = spl[0]
        dst = spl[2]
        distances[(src, dst)] = distances[(dst, src)] = int(spl[-1])
    return distances


def main(input_file):
    distances = parse_input(input_file)
    costs = [
        sum(distances[(src, dst)] for src, dst in zip(order, order[1:]))
        for order in itertools.permutations({src for src, dst in distances})
    ]
    print("Part 1:", min(costs))
    print("Part 2:", max(costs))


if __name__ == '__main__':
    main(sys.argv[1])
