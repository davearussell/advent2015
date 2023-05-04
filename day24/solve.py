#! /usr/bin/python3
import json
import sys
from functools import reduce

import numpy
import numba


@numba.njit(cache=True)
def find_all_groups(values, target):
    groups = numpy.zeros(1000000, dtype=numpy.uint32)
    count = 0
    for g in range(1 << len(values)):
        n = w = 0
        for j in range(len(values)):
            if g & (1 << j):
                n += 1
                w += values[j]
                if w > target:
                    break
        if w == target:
            groups[count] = g
            count += 1
    return groups[:count]


def qe(group, values):
    v = 1
    for i in range(32):
        if group & (1 << i):
            v *= values[i]
    return v


def fmt(group, values):
    return ','.join(str(values[i]) for i in range(32) if group & (1 << i))


def can_partition(group, groups, n):
    if n == 2:
        return True
    compatible = groups[numpy.where(groups & group == 0)]
    return len(compatible) >= n - 1 and can_partition(compatible[0], compatible, n - 1)


def solve(values, n_groups):
    target = sum(values) // n_groups
    arr = find_all_groups(values, target).tolist()
    tmp = sorted([int(g) for g in arr], key=lambda x: (x.bit_count(), qe(x, values)))
    groups = numpy.array(tmp, dtype=numpy.uint32)
    for group in groups:
        if can_partition(group, groups, n_groups):
            return qe(group, values)


def main(input_file):
    values = numpy.array([int(v) for v in open(input_file).read().split()],
                         dtype=numpy.uint32)

    import time
    t0 = time.time()
    print("Part 1:", solve(values, 3))
    t1 = time.time()
    print("# in %.1fs" % (t1 - t0))
    print()
    
    print("Part 2:", solve(values, 4))
    t2 = time.time()
    print("# in %.1fs" % (t2 - t1))


if __name__ == '__main__':
    main(sys.argv[1])
