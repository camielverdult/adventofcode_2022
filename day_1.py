calories = []
index = 0

with open("input.txt", 'r') as f:
    for line in f.readlines():
        if line == '\n':
            index += 1
        else:
            if len(calories) < index + 1:
                calories.append(int(line))
            else:
                calories[index] += int(line)

calories = sorted(calories, reverse=True)

print("Most calories carried by elf: ", calories[0])
print("Sum of calories carried by top 3 elfs: ", sum(calories[0:3]))
