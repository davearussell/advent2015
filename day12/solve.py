#! /usr/bin/python3
import json
import sys


def rsum(x, skip_red=False):
    if isinstance(x, int):
        return x
    elif isinstance(x, str):
        return 0
    elif isinstance(x, list):
        return sum(rsum(v, skip_red) for v in x)
    elif isinstance(x, dict):
        values = x.values()
        if skip_red and 'red' in values:
            return 0
        return sum(rsum(v, skip_red) for v in values)
    else:
        assert 0, x


def main(input_file):
    data = json.load(open(input_file))
    print("Part 1:", rsum(data, False))
    print("Part 2:", rsum(data, True))



if __name__ == '__main__':
    main(sys.argv[1])
