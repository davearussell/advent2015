#! /usr/bin/python3
import sys


def parse_input(path):
    ingredients = []
    for line in open(path).read().strip().split('\n'):
        name, properties = line.split(': ')
        ingredient = {'name': name}
        for prop in properties.split(','):
            k, v = prop.split()
            ingredient[k] = int(v)
        ingredients.append(ingredient)
    return ingredients


def score(ingredients, recipe):
    score = 1
    for k in ['capacity', 'durability', 'flavor', 'texture']:
        score *= max(0, sum(ing[k] * n for ing, n in zip(ingredients, recipe)))
    calories = sum(ing['calories'] * n for ing, n in zip(ingredients, recipe))
    return score, calories


def main(input_file):
    ingredients = parse_input(input_file)
    part1 = part2 = 0
    for a in range(100):
        for b in range(100 - a):
            for c in range(100 - a - b):
                n += 1
                d = 100 - a - b - c
                rscore, calories = score(ingredients, [a, b, c, d])
                part1 = max(part1, rscore)
                if calories == 500:
                    part2 = max(part2, rscore)
    print("Part 1:", part1)
    print("Part 2:", part2)


if __name__ == '__main__':
    main(sys.argv[1])
