
def part1(lines):
    p1_points, p2_points = 0, 0

    for line in lines:
        moves = line.strip().split(" ")
        p1_move = ord(moves[0]) - 64
        p2_move = ord(moves[1]) - 87


        p1_points += p1_move
        p2_points += p2_move

        # A, Y: Rock     (1)
        # B, X: Paper    (2)
        # C, Z: Scissors (3)a
        if (p1_move == p2_move):
            p1_points += 3
            p2_points += 3
        elif (p1_move == 1 and p2_move == 2):
            # P2 wins with paper eats rock
            p2_points += 6
        elif (p1_move == 1 and p2_move == 3):
            # P1 wins with rock obliterating scissors
            p1_points += 6
        elif (p1_move == 2 and p2_move == 1):
            # P1 wins with paper eats rock
            p1_points += 6
        elif (p1_move == 2 and p2_move == 3):
            # P2 wins with scissors eats paper
            p2_points += 6
        elif (p1_move == 3 and p2_move == 1):
            # P2 wins with rock annihilating scissors 
            p2_points += 6
        elif (p1_move == 3 and p2_move == 2):
            # P1 wins with scissors annihilating paper 
            p1_points += 6

    print(f"part one: p1 points: {p1_points}, p2 points: {p2_points}")

def part2(lines):
    # THIS DOES NOT WORK
    p1_points, p2_points = 0, 0
    round_count = 0

    for line in lines:
        moves = line.strip().split(" ")
        p1_move = ord(moves[0]) - 64

        p1_points += p1_move

        if (round_count == 3):
            # We win
            p2_points += 6
            round_count = 0

            if (p1_move == 1):
                p2_points += 2
            elif (p1_move == 2):
                p2_points += 3
            else:
                p2_points += 1

            continue

        if (p1_move == 1):
            # We draw
            p1_points += 3
            p2_points += 3 + 1
        elif (p1_move == 2):
            # We lose
            p1_points += 6
            p2_points += 1
        
        round_count += 1

    print(f"part two: p1 points: {p1_points}, p2 points: {p2_points}")


if __name__ == "__main__":
    with open("input.txt", 'r') as f:
        lines = f.readlines()
        part1(lines)
        part2(lines)