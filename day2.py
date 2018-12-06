from collections import Counter
from itertools import product


def part1():
    count2 = 0
    count3 = 0

    with open("assets/day2_input") as f:
        for line in f:
            if n_of_any_letter(line, 2):
                count2 += 1
            if n_of_any_letter(line, 3):
                count3 += 1

    print(count2 * count3)


def part2():
    with open("assets/day2_input") as f:
        box_ids = f.read().splitlines()

    for id1, id2 in product(box_ids, repeat=2):
        if differ_by_one(id1, id2):
            print("".join(c1 for c1, c2 in zip(id1, id2) if c1 == c2))
            return

    print("No matching IDs found")


def n_of_any_letter(s, n):
    counter = Counter(s)
    for _, count in counter.most_common():
        if count == n:
            return True
    return False


def differ_by_one(s1, s2):
    diffs = 0

    # Assume they are of the same length.
    for c1, c2 in zip(s1, s2):
        if c1 != c2:
            diffs += 1

    return diffs == 1


part2()
