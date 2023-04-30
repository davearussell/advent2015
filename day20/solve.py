#! /usr/bin/python3
import sys


def find_primes(limit):
    is_prime = [True] * limit
    for p in range(2, limit):
        if is_prime[p]:
            m = p * 2
            while m < limit:
                is_prime[m] = False
                m += p
    return [i for i in range(2, limit) if is_prime[i]]

# NOTE: To reduce runtime we discount any number whose largest prime factor
# is greater than 100. Numbers with big prime factors have a much smaller
# sum of factors than those with smaller ones, so ignoring them is OK.
# For my input, the solution's largest prime factor was 11.
PRIMES = find_primes(100)


def prime_factors(n):
    pfs = []
    for prime in PRIMES:
        d, m = divmod(n, prime)
        if m:
            continue
        n = d
        pfs.append([prime, 1])
        while True:
            d, m = divmod(n, prime)
            if m:
                break
            pfs[-1][-1] += 1
            n = d
        if n == 1:
            return pfs
    return []


def sum_of_factors(n):
    pfs = prime_factors(n)
    n = 1
    for f, count in pfs:
        v = 0
        for i in range(count + 1):
            v += (f ** i)
        n *= v
    return n


def part1(target):
    n = 1
    while True:
        if sum_of_factors(n) * 10 >= target:
            return n
        n += 1


def part2(target):
    n = 1
    while True:
        if sum(n // i for i in range(1, 51) if not n % i) * 11 > target:
            return n
        n += 1


def main(input_file):
    target = int(open(input_file).read())
    print("Part 1:", part1(target))
    print("Part 2:", part2(target))


if __name__ == '__main__':
    main(sys.argv[1])
