#! /usr/bin/python3
import sys


def parse_input(path):
    insns = []
    for line in open(path).read().strip().split('\n'):
        spl = line.replace(',', '').split()
        op = spl[0]
        args = spl[1:]
        for i in range(len(args)):
            if args[i] not in 'ab':
                args[i] = int(args[i])
        insns.append((op, args))
    return insns


def solve(a):
    b = 0
    while a > 1:
        b += 1
        if a & 1:
            a = a * 3 + 1
        else:
            a //= 2
    return b


def get_initial_a(insns, a):
    regs = {'a': a, 'b': 0}
    i = 0
    while not regs['b']:
        insn, args = insns[i]
        if insn == 'hlf':
            regs[args[0]] //= 2
        elif insn == 'tpl':
            regs[args[0]] *= 3
        elif insn == 'inc':
            regs[args[0]] += 1
        elif insn == 'jmp':
            i += args[0] - 1
        elif insn == 'jie':
            if not regs[args[0]] & 1:
                i += args[1] - 1
        elif insn == 'jio':
            if regs[args[0]] == 1:
                i += args[1] - 1
        else:
            assert 0, (insn, args)
        i += 1
    return regs['a']


def main(input_file):
    insns = parse_input(input_file)
    print("Part 1:", solve(get_initial_a(insns, 0)))
    print("Part 2:", solve(get_initial_a(insns, 1)))


if __name__ == '__main__':
    main(sys.argv[1])
