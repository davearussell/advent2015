#! /usr/bin/python3
import sys


def parse_input(path):
    runners = []
    for line in open(path).read().strip().split('\n'):
        spl = line.split()
        speed = int(spl[3])
        run_time = int(spl[6])
        rest_time = int(spl[-2])
        runners.append((speed, run_time, run_time + rest_time))
    return runners


def distance_travelled(runner, duration):
    speed, run_time, period = runner
    cycles, rem = divmod(duration, period)
    return cycles * (speed * run_time) + min(run_time, rem) * speed


def part2(runners, duration):
    scores = [0] * len(runners)
    distances = [0] * len(runners)
    for t in range(duration):
        for i, (speed, run_time, period) in enumerate(runners):
            if t % period < run_time:
                distances[i] += speed
        max_dist = max(distances)
        for i, distance in enumerate(distances):
            if distance == max_dist:
                scores[i] += 1
    return max(scores)


def main(input_file):
    runners = parse_input(input_file)
    duration = 2503
    print("Part 1:", max(distance_travelled(runner, duration) for runner in runners))
    print("Part 2:", part2(runners, duration))


if __name__ == '__main__':
    main(sys.argv[1])
