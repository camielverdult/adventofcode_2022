
def ord_value(char) -> int:
    if 65 <= ord(char) <= 90:
        return ord(char) - 38
    elif 97 <= ord(char) <= 122:
        return ord(char) - 96
    print("wtf")
    return -100000

def first_part(lines: list):
    rucksack_priority_sum = 0
    for line in lines:
        halfway = round(len(line) / 2 - 0.5)
        first = set(line[:halfway].strip())
        second = set(line[halfway:].strip())

        overlap = first.intersection(second)

        if not overlap:
            continue

        priority = max([ord_value(x) for x in overlap])
        rucksack_priority_sum += priority
        print(f"{line.strip()}: {line[:halfway].strip()} + {line[halfway:].strip()}, {overlap}: {priority}")

    print(f"PART 1: Priority sum: {rucksack_priority_sum}")

def second_part(lines: list[str]):
    groups: list[set] = []
    group_index = 1
    badge_sum = 0
    for line in lines:
        groups.append(set(line.strip()))

        if len(groups) == 3:
            badge = groups[0].intersection(groups[1], groups[2]).pop()
            print(f"{group_index}-{group_index+2}: {badge}")
            groups = []
            group_index += 3
            badge_sum += ord_value(badge)

    print(f"PART 2: Badge sum: {badge_sum}")

if __name__ == "__main__":
    with open("input.txt", 'r') as f:
        lines = f.readlines()

    first_part(lines)
    second_part(lines)