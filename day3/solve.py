#! /usr/bin/python3
import sys

OFFSETS = {'^': (0, -1), 'v': (0, 1), '<': (-1, 0), '>': (1, 0)}


def visit_houses(moves, n_santas):
    start = (0, 0)
    poses = [start for _ in range(n_santas)]
    visited = {start}
    for i, move in enumerate(moves):
        idx = i % n_santas
        dx, dy = OFFSETS[move]
        poses[idx] = (poses[idx][0] + dx, poses[idx][1] + dy)
        visited.add(poses[idx])
    return len(visited)


def main(input_file):
    moves = open(input_file).read().strip()
    for i in [1, 2]:
        print("Part %d: %d" % (i,  visit_houses(moves, i)))


if __name__ == '__main__':
    main(sys.argv[1])
