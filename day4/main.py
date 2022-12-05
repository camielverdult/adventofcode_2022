def unpack(range_: str) -> set:
    start_finish = range_.split("-")
    return set(x for x in range(int(start_finish[0]), int(start_finish[1]) + 1))

def first_part(lines: list[str]):
    overlaps = 0
    for line in lines:
        parts = line.strip().split(",")
        first = set(unpack(parts[0]))
        second = set(unpack(parts[1]))
        
        if first.issubset(second) or second.issubset(first):
            overlaps += 1
        
    print(f"PART 1: {overlaps} pair overlaps,")

def second_part(lines: list[str]):
    total = 0

    for line in lines:
        parts = line.strip().split(",")
        first = set(unpack(parts[0]))
        second = set(unpack(parts[1]))
        
        if first.intersection(second):
            total += 1
        
    print(f"PART 2: {total} overlapping work")

if __name__ == "__main__":
    with open("input.txt", 'r') as f:
        lines = f.readlines()

    first_part(lines)
    second_part(lines)