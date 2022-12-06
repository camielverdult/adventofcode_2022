def find_marker(line: str, unique_chars: int, diversion: int):
    distinct = []
    for char_i in range(len(line)):
        char = line[char_i]
        
        if char not in distinct:
            distinct.append(char)

            if len(distinct) == unique_chars:
                return f"first {unique_chars} unique char marker after character {char_i + diversion}"
        else:
            distinct.clear()

if __name__ == "__main__":
    with open("input.txt", 'r') as f:
        for line in f.readlines():
            print("1. {}".format(find_marker(line, 4, 0)))
            print("2. {}\n".format(find_marker(line, 14, 0)))