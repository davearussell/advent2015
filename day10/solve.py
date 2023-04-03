#! /usr/bin/python3
import sys


def iterate(s):
    output = ''
    digit = count = None
    for char in s:
        if char == digit:
            count += 1
        else:
            if digit:
                output += '%d%s' % (count, digit)
            digit = char
            count = 1
    return output + '%d%s' % (count, digit)


def main(input_file):
    seq = open(input_file).read().strip()
    
    for i in range(40):
        print(i, len(seq))
        seq = iterate(seq)
    print("Part 1:", len(seq))
    
    for i in range(10):
        print(i + 40, len(seq))
        seq = iterate(seq)
    print("Part 2:", len(seq))


if __name__ == '__main__':
    main(sys.argv[1])
