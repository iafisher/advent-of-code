from collections import Counter, defaultdict
from operator import itemgetter


def part1():
    minutes_per_guard = get_minutes_per_guard()

    sleepiest_guard, _ = max(
        minutes_per_guard.items(), key=lambda pair: sum(pair[1].values())
    )
    most_common_minute = minutes_per_guard[sleepiest_guard].most_common(1)[0][0]
    return int(sleepiest_guard) * most_common_minute


def part2():
    minutes_per_guard = get_minutes_per_guard()

    max_guard = None
    max_guard_minute = None
    max_guard_minute_count = 0
    for guard, counter in minutes_per_guard.items():
        for minute, count in counter.items():
            if count > max_guard_minute_count:
                max_guard = guard
                max_guard_minute = minute
                max_guard_minute_count = count

    return int(max_guard) * max_guard_minute


def get_minutes_per_guard():
    """Return a dictionary mapping from guard IDs to Counter objects, whose keys are
    the minutes that the guard is asleep and whose values are the number of times the
    guard is asleep at that minute.
    """
    events = []
    with open("assets/day4_input") as f:
        for line in f:
            time, msg = line.split("] ", maxsplit=1)
            time = time[1:]
            events.append( (time, msg) )

    events.sort(key=itemgetter(0))

    # Map from guards -> (minute -> number of times asleep)
    # minutes_per_guard["1667"][23] == 7 indicates that Guard #1667 was asleep seven
    # times at the 23rd minute.
    minutes_per_guard = defaultdict(Counter)

    start = None
    guard = None
    for time, msg in events:
        if msg.startswith("Guard"):
            guard = msg.split()[1][1:]
        elif msg.startswith("falls"):
            start = int(time[-2:])
        elif msg.startswith("wakes"):
            for x in range(start, int(time[-2:])):
                minutes_per_guard[guard][x] += 1

    return minutes_per_guard


print(part2())
