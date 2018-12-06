import string


def part1():
    with open("assets/day5_input") as f:
        polymer = f.read().strip()

    return len(collapse_polymer(polymer))


def part2():
    with open("assets/day5_input") as f:
        polymer = f.read().strip()

    best_letter = None
    best_letter_size = float("inf")
    for letter in string.ascii_lowercase:
        stripped_polymer = polymer.replace(letter, "").replace(letter.upper(), "")
        this_letter_size = len(collapse_polymer(stripped_polymer))
        if this_letter_size < best_letter_size:
            best_letter = letter
            best_letter_size = this_letter_size

    return best_letter_size


def collapse_polymer(polymer):
    polymer_list = list(polymer)
    i = 0
    while i < len(polymer_list) - 1:
        if can_react(polymer_list[i], polymer_list[i+1]):
            polymer_list.pop(i)
            polymer_list.pop(i)
            if i > 0:
                i -= 1
        else:
            i += 1
    return "".join(polymer_list)


def can_react(a, b):
    return a.lower() == b.lower() and a.isupper() != b.isupper()


print(part2())
