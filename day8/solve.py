#! /usr/bin/python3
import sys


def unescape(word):
    s = ''
    assert word[0] == word[-1] == '"'
    word = list(word[1:-1])
    while word:
        char = word.pop(0)
        if char == '\\':
            escape_char = word.pop(0)
            if escape_char in '\\"':
                s += escape_char
            elif escape_char == 'x':
                code, word = word[:2], word[2:]
                s += chr(int(''.join(code), base=16))
            else:
                assert 0, word
        else:
            s += char
    return s


def escape(word):
    s = ''
    for char in word:
        if char in '\\"':
            s += '\\'
        s += char
    return '"%s"' % s


def main(input_file):
    words = open(input_file).read().split()
    unescaped = [unescape(word) for word in words]
    escaped = [escape(word) for word in words]
    print("Part 1:", sum(map(len, words)) - sum(map(len, unescaped)))
    print("Part 2:", sum(map(len, escaped)) - sum(map(len, words)))


if __name__ == '__main__':
    main(sys.argv[1])
