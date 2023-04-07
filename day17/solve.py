#! /usr/bin/python3
import sys


def main(input_file):
    containers = [int(x) for x in open(input_file).read().split()]
    n = len(containers)
    counts = [0] * n
    for v in range(1 << n):
        indices = [x for x in range(n) if v & (1 << x)]
        if sum([containers[i] for i in indices]) == 150:
            counts[len(indices)] += 1
    print("Part 1:", sum(counts))
    print("Part 2:", [c for c in counts if c][0])


if __name__ == '__main__':
    main(sys.argv[1])
