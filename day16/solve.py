#! /usr/bin/python3
import sys


FACTS = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1,
}
GT = {'cats', 'trees'}
LT = {'pomeranians', 'goldfish'}



def parse_input(path):
    sues = []
    for line in open(path).read().strip().split('\n'):
        sue = {}
        things = line.split(':', 1)[1]
        for thing in things.split(','):
            k, v = thing.strip().split(':')
            sue[k] = int(v)
        sues.append(sue)
    return sues


def part1_match(sue):
    return all(v == FACTS[k] for k, v in sue.items())


def part2_match(sue):
    for k, v in sue.items():
        if k in GT:
            if v <= FACTS[k]:
                return False
        elif k in LT:
            if v >= FACTS[k]:
                return False
        elif v != FACTS[k]:
            return False
    return True


def main(input_file):
    sues = parse_input(input_file)

    for i, sue in enumerate(sues):
        if part1_match(sue):
            print("Part 1:", i + 1)
        if part2_match(sue):
            print("Part 2:", i + 1)


if __name__ == '__main__':
    main(sys.argv[1])
