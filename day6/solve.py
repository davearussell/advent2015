#! /usr/bin/python3
import sys
import numpy


def parse_input(path):
    orders = []
    for line in open(path).read().replace('turn ', '').strip().split('\n'):
        spl = line.split()
        action = spl[0]
        x0, y0 = map(int, spl[1].split(','))
        x1, y1 = map(int, spl[3].split(','))
        orders.append((action, (x0, y0), (x1, y1)))
    return orders


def part1(action, region):
    if action == 'on':
        region.fill(1)
    elif action == 'off':
        region.fill(0)
    else:
        region ^= 1


def part2(action, region):
    if action == 'on':
        region += 1
    elif action == 'off':
        region[region > 0] -= 1
    else:
        region += 2


def follow_orders(orders, logic):
    lights = numpy.zeros([1000, 1000], dtype=numpy.int16)
    for action, (x0, y0), (x1, y1) in orders:
        region = lights[x0 : x1+1, y0 : y1+1]
        logic(action, region)
    return numpy.sum(lights)


def main(input_file):
    orders = parse_input(input_file)
    print("Part 1:", follow_orders(orders, part1))
    print("Part 2:", follow_orders(orders, part2))


if __name__ == '__main__':
    main(sys.argv[1])
