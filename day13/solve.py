#! /usr/bin/python3
import itertools
import sys


def parse_input(path):
    rules = {}
    for line in open(path).read().strip().split('\n'):
        spl = line.split()
        sitter = spl[0]
        sign = 1 if spl[2] == 'gain' else -1
        value = sign * int(spl[3])
        sittee = spl[-1].rstrip('.')
        rules[(sitter, sittee)] = value
    net = {}
    for a, b in rules:
        net[(a, b)] = net[(b, a)] = rules[(a, b)] + rules[(b, a)]
    return net


def happiness(rules):
    return max([
        sum(rules[(a, b)] for a, b in zip(order, list(order[1:]) + [order[0]]))
        for order in itertools.permutations({a for a, b in rules})
    ])


def main(input_file):
    rules = parse_input(input_file)
    print("Part 1:", happiness(rules))

    for person in {a for a, b in rules}:
        rules[('me', person)] = rules[(person, 'me')] = 0
    print("Part 2:", happiness(rules))
    


if __name__ == '__main__':
    main(sys.argv[1])
