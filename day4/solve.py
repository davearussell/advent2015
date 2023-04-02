#! /usr/bin/python3
import hashlib
import sys


def main(input_file):
    secret = open(input_file).read().strip().encode()
    i = 1
    part1 = False
    while True:
        md5 = hashlib.md5(b'%s%d' % (secret, i)).hexdigest()
        if md5.startswith('00000') and not part1:
            print("Part 1:", i)
            part1 = True
        if md5.startswith('000000'):
            print("Part 2:", i)
            break
        i += 1


if __name__ == '__main__':
    main(sys.argv[1])
