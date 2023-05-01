#! /usr/bin/python3

P_HP = 50
P_MANA = 500

B_HP = 51
B_DMG = 9

MISSILE_COST = 53
MISSILE_DMG = 4

DRAIN_COST = 73
DRAIN_DMG = 2

SHIELD_COST = 113
SHIELD_ARMOR = 7
SHIELD_LEN = 6

POISON_COST = 173
POISON_DMG = 3
POISON_LEN = 6

RECHARGE_COST = 229
RECHARGE_REGEN = 101
RECHARGE_LEN = 5


def act(state, action, hard_mode):
    p_hp, b_hp, p_mana, shield, poison, recharge, spent = state

    # 1. Hard mode damage ticks
    if hard_mode:
        p_hp -= 1
        if p_hp <= 0:
            return None

    # 2. Player acts
    if action == 'missile':
        if p_mana < MISSILE_COST:
            return None
        spent += MISSILE_COST
        p_mana -= MISSILE_COST
        b_hp -= MISSILE_DMG
    elif action == 'drain':
        if p_mana < DRAIN_COST:
            return None
        spent += DRAIN_COST
        p_mana -= DRAIN_COST
        p_hp += DRAIN_DMG
        b_hp -= DRAIN_DMG
    elif action == 'shield':
        if shield or p_mana < SHIELD_COST:
            return None
        spent += SHIELD_COST
        p_mana -= SHIELD_COST
        shield = SHIELD_LEN
    elif action == 'poison':
        if poison or p_mana < POISON_COST:
            return None
        spent += POISON_COST
        p_mana -= POISON_COST
        poison = POISON_LEN
    elif action == 'recharge':
        if recharge or p_mana < RECHARGE_COST:
            return None
        spent += RECHARGE_COST
        p_mana -= RECHARGE_COST
        recharge = RECHARGE_LEN
    else:
        assert 0, action

    if b_hp <= 0:
        return (p_hp, 0, p_mana, shield, poison, recharge, spent)

    # 3. Effects tick
    if shield:
        shield -= 1
    if recharge:
        recharge -= 1
        p_mana += RECHARGE_REGEN
    if poison:
        poison -= 1
        b_hp -= POISON_DMG
        if b_hp <= 0:
            return (p_hp, 0, p_mana, shield, poison, recharge, spent)

    # 4. Boss attacks
    dmg = (B_DMG - (SHIELD_ARMOR if shield else 0))
    p_hp -= dmg
    if p_hp < 0:
        return None

    # 5. Effects tick
    if shield:
        shield -= 1
    if recharge:
        recharge -= 1
        p_mana += RECHARGE_REGEN
    if poison:
        poison -= 1
        b_hp -= POISON_DMG
        if b_hp < 0:
            b_hp = 0

    return (p_hp, b_hp, p_mana, shield, poison, recharge, spent)


def cheapest_win(hard_mode):
    initial_state = (P_HP, B_HP, P_MANA, 0, 0, 0, 0)
    states = {initial_state}
    best = 1000000
    while states:
        next_states = set()
        for state in states:
            for action in ['missile', 'drain', 'shield', 'poison', 'recharge']:
                next_state = act(state, action, hard_mode)
                if next_state:
                    if next_state[-1] < best:
                        if not next_state[1]:
                            best = next_state[-1]
                        else:
                            next_states.add(next_state)
        states = next_states
    return best


if __name__ == '__main__':
    print("Part 1:", cheapest_win(hard_mode=False))
    print("Part 2:", cheapest_win(hard_mode=True))
