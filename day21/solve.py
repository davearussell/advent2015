#! /usr/bin/python3
import sys
import yaml

WEAPONS = [
    (8,  4, 0),
    (10, 5, 0),
    (25, 6, 0),
    (40, 7, 0),
    (74, 8, 0),
]

ARMOR = [
    (13,  0, 1),
    (31,  0, 2),
    (53,  0, 3),
    (75,  0, 4),
    (102, 0, 5),
]

RINGS = [
    (0,   0, 0),
    (25,  1, 0),
    (50,  2, 0),
    (100, 3, 0),
    (20,  0, 1),
    (40,  0, 2),
    (80,  0, 3),
]


def player_hp_left(p_hp, p_dmg, p_arm, b_hp, b_dmg, b_arm):
    p_eff = max(1, p_dmg - b_arm)
    b_eff = max(1, b_dmg - p_arm)
    p_rounds = (b_hp + p_eff - 1) // p_eff
    return p_hp - (p_rounds - 1) * b_eff


def main(input_file):
    boss = yaml.load(open(input_file))
    b_hp = boss['Hit Points']
    b_dmg = boss['Damage']
    b_armor = boss['Armor']

    p_hp = 100

    min_win = 1000
    max_lose = 0
    for c1, d1, a1 in WEAPONS:
        for c2, d2, a2 in ARMOR:
            for c3, d3, a3 in RINGS:
                for c4, d4, a4 in RINGS:
                    if c3 == c4 and c3 > 0:
                        continue
                    c = c1 + c2 + c3 + c4
                    d = d1 + d2 + d3 + d4
                    a = a1 + a2 + a3 + a4
                    left = player_hp_left(p_hp, d, a, b_hp, b_dmg, b_armor)
                    if left > 0:
                        if c < min_win:
                            min_win = c
                    elif c > max_lose:
                        max_lose = c
    print("Part 1:", min_win)
    print("Part 2:", max_lose)


if __name__ == '__main__':
    main(sys.argv[1])
