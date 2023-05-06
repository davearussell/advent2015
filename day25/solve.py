#! /usr/bin/python3
import sys

C1 = 20151125
M = 252533
D = 33554393


def parse_input(path):
    words = open(path).read().replace(',', '').replace('.', '').split()
    return [int(w) for w in words if w.isdigit()]


def index(row, col):
    diagonal = row + col - 1
    last_i = ((diagonal + 1) * diagonal) // 2
    return last_i - row + 1


def code_at_index(idx):
    code = C1
    for i in range(idx - 1):
        code = (code * M) % D
    return code


def main(input_file):
    row, col = parse_input(input_file)
    idx = index(row, col)
    print(code_at_index(idx))


if __name__ == '__main__':
    main(sys.argv[1])
