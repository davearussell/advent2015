#! /usr/bin/python3
import sys


def maybe_int(s):
    return int(s) if s.isdigit() else s


OPS = {
    'SET': lambda a: a,
    'NOT': lambda a: (~a) & 0xffff,
    'AND': lambda a, b: a & b,
    'OR': lambda a, b: a | b,
    'LSHIFT': lambda a, b:  (a << b) & 0xffff,
    'RSHIFT': lambda a, b:  a >> b,
}


def parse_input(path):
    signals = {}
    for line in open(path).read().strip().split('\n'):
        words = line.split()
        expr = words[:-2]
        assert words[-2] == '->', repr(line)
        dst = words[-1]
        if len(expr) == 1:
            signals[dst] = ('SET', (maybe_int(expr[0]),))
        elif len(expr) == 2:
            signals[dst] = (expr[0], (maybe_int(expr[1]),))
        else:
            signals[dst] = (expr[1], (maybe_int(expr[0]), maybe_int(expr[2])))
    return signals


def resolve_signals(signals):
    resolved = {}
    unresolved = signals.copy()
    while len(resolved) < len(signals):
        for signal in signals:
            if signal in resolved:
                continue
            op, args = signals[signal]
            values = [arg if isinstance(arg, int) else resolved.get(arg) for arg in args]
            if None not in values:
                resolved[signal] = OPS[op](*values)
    return resolved


def main(input_file):
    signals = parse_input(input_file)
    resolved = resolve_signals(signals)
    print("Part 1:", resolved['a'])

    p2_signals = dict(signals, b=('SET', (resolved['a'],)))
    p2_resolved = resolve_signals(p2_signals)
    print("Part 2:", p2_resolved['a'])


if __name__ == '__main__':
    main(sys.argv[1])
