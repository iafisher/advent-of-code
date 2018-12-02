def part1():
    freq = 0

    with open("assets/day1_input") as f:
        for line in f:
            freq += int(line)

    print(freq)


def part2():
    freq = 0

    with open("assets/day1_input") as f:
        changes = [int(line) for line in f]

    seen = set([freq])
    while True:
        for change in changes:
            freq += change
            if freq in seen:
                print("First duplicate frequency:", freq)
                return
            else:
                seen.add(freq)


part2()
