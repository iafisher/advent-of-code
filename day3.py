import re
from collections import defaultdict


def part1():
    counts = defaultdict(int)

    with open("assets/day3_input") as f:
        for line in f:
            _, _, pos, dim = line.split()
            from_left, from_top = pos.split(",")
            width, height = dim.split("x")
            from_top = from_top[:-1]  # Remove trailing colon.
            for x in range(int(from_left), int(from_left) + int(width)):
                for y in range(int(from_top), int(from_top) + int(height)):
                    counts[(x, y)] += 1

    more_than_one = 0
    for key, val in counts.items():
        if val > 1:
            more_than_one += 1
    return more_than_one


def part2():
    claims = defaultdict(list)
    eligible = set()

    with open("assets/day3_input") as f:
        for line in f:
            myid, _, pos, dim = line.split()
            from_left, from_top = pos.split(",")
            width, height = dim.split("x")
            from_top = from_top[:-1]  # Remove trailing colon.

            eligible.add(myid)

            for x in range(int(from_left), int(from_left) + int(width)):
                for y in range(int(from_top), int(from_top) + int(height)):
                    claims[(x, y)].append(myid)

    for _, claimlist in claims.items():
        if len(claimlist) > 1:
            for claim in claimlist:
                eligible.discard(claim)

    if len(eligible) == 1:
        return eligible.pop()
    else:
        return None


print(part2())
