def first_part(lines: list[str]):
    # Find stack amount
    stack_n = -1
    for line in lines:
        try:
            stack_n = int(line.replace(" ", "").strip())
            stack_n = int(str(stack_n)[-1])
            break
        except:
            continue

    # Build stack table
    stacks = [[] for _ in range(stack_n)]
    # print(f"{stack_n} stacks: {stacks}")
    move_start_i = 0
    for line_i in range(len(lines)):

        line = lines[line_i]

        # Add moves until we reach the stack index legend line
        if line.startswith(" 1   2"):
            move_start_i = line_i + 2
            break

        # Extract character
        char_i = 0
        for char in line.split(" "):
            if char != "":
                stacks[char_i].append(char)

            # print(f"{line} -> {stacks}")
            char_i += 1
    
    # Do moves
    # print(stacks)
    for line_i in range(move_start_i, len(lines)):
        line = lines[line_i]
        instructions = []

        for part in line.split(" "):
            try:
                instructions.append(int(part))
            except:
                continue

        quantity = instructions[0]
        source = instructions[1] - 1
        to = instructions[2] - 1
        # print(f"move {quantity} from {source} -> {to}")

        for value in stacks[source][0:quantity]:
            stacks[to].insert(0, value)
            stacks[source].remove(value)
            # print(stacks)
        
    print("FIRST: Crates on top: " + "".join([x[0] for x in stacks]))

def second_part(lines: list[str]):
    # Find stack amount
    stack_n = -1
    for line in lines:
        try:
            stack_n = int(line.replace(" ", "").strip())
            stack_n = int(str(stack_n)[-1])
            break
        except:
            continue

    # Build stack table
    stacks = [[] for _ in range(stack_n)]
    # print(f"{stack_n} stacks: {stacks}")
    move_start_i = 0
    for line_i in range(len(lines)):

        line = lines[line_i]

        # Add moves until we reach the stack index legend line
        if line.startswith(" 1   2"):
            move_start_i = line_i + 2
            break

        # Extract character
        char_i = 0
        for char in line.split(" "):
            if char != "":
                stacks[char_i].append(char)

            # print(f"{line} -> {stacks}")
            char_i += 1
    
    # Do moves
    # print(stacks)
    for line_i in range(move_start_i, len(lines)):
        line = lines[line_i]
        instructions = []

        for part in line.split(" "):
            try:
                instructions.append(int(part))
            except:
                continue

        quantity = instructions[0]
        source = instructions[1] - 1
        to = instructions[2] - 1
        print(f"move {quantity} from {source} -> {to}")

        for value in reversed(stacks[source][0:quantity]):
            stacks[to].insert(0, value)
            stacks[source].remove(value)

        print(stacks)
        
    print("SECOND: " + "".join([x[0] for x in stacks]))

if __name__ == "__main__":
    with open("input.txt", 'r') as f:
        lines = [x.replace("[", "").replace("]", "").strip('\n').replace("    ", " ") for x in f.readlines()]

    first_part(lines)
    second_part(lines)