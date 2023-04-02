#! /usr/bin/python3
import sys


def is_nice(word):
    bad = {('a', 'b'), ('c', 'd'), ('p', 'q'), ('x', 'y')}
    vowels = 0
    double = False
    prev = None
    for char in word:
        if (prev, char) in bad:
            return False
        if char == prev:
            double = True
        prev = char
        vowels += (char in 'aeiou')
    return double and vowels >= 3


def is_really_nice(word):
    pairs = {}
    has_xyx = False
    has_repeat = False
    for i, char in enumerate(word):
        if i >= 2 and char == word[i - 2]:
            has_xyx = True
        if i >= 1:
            pair = word[i-1:i+1]
            l = pairs.setdefault(pair, [])
            l.append(i)
            if len(l) > 2 or len(l) == 2 and l[0] < i - 1:
                has_repeat = True
    return has_xyx and has_repeat


def count_nice(words, predicate):
    return len([word for word in words if predicate(word)])


def main(input_file):
    words = open(input_file).read().split()
    print("Part 1:", count_nice(words, is_nice))
    print("Part 2:", count_nice(words, is_really_nice))


if __name__ == '__main__':
    main(sys.argv[1])
