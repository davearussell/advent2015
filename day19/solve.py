#! /usr/bin/python3
import sys
import re


def split_molecule(mol):
    atoms = []
    current = ''
    for char in mol:
        if char.isupper():
            if current:
                atoms.append(current)
            current = char
        else:
            current += char
    if current:
        atoms.append(current)
    return atoms


def parse_input(path):
    swaps = {}
    target = None
    
    for line in open(path):
        if ' => ' in line:
            src, dst = line.strip().split(' => ')
            swaps.setdefault(src, []).append(dst)
        elif line.strip():
            target = line.strip()
            
    return swaps, target


def count_swaps(swaps, molecule):
    seen = set()
    n = 0
    atoms = split_molecule(molecule)

    for i, atom in enumerate(atoms):
        if atom in swaps:
            for swap in swaps[atom]:
                tmp = atoms.copy()
                tmp[i] = swap
                new_mol = ''.join(tmp)
                if new_mol not in seen:
                    n += 1
                    seen.add(new_mol)
    return n


def steps_to_make(swaps, molecule):
    reductions = {end: start for start, ends in swaps.items() for end in ends}
    steps = 0
    while len(molecule) > 1:
        for e, s in reductions.items():
            if e in molecule:
                molecule = molecule.replace(e, s, 1)
                steps += 1
                break
        else:
            assert 0, molecule
    return steps


def main(input_file):
    swaps, target = parse_input(input_file)
    print("Part 1:", count_swaps(swaps, target))

    p2_swaps, p2_target = parse_input('part2.txt')
    print("Part 2:", steps_to_make(p2_swaps, p2_target))


if __name__ == '__main__':
    main(sys.argv[1])
