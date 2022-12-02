#A rock, B paper, C scissor
#X need to lose, Y need to draw, Z need to win
#score: 1 rock, 2 paper, 3 scissor + 0 lose, 3 draw, 6 win
outcomes = {
        "A": ["C", "A", "B"],
        "B": ["A", "B", "C"],
        "C": ["B", "C", "A"] 
    }
with open("./input/input.txt") as file:
    total_score = 0
    for line in file:
        round = line.strip().split(" ")
        print("round:", round)
        if round[1] == "Z":
            my_pick = outcomes[round[0]][2]
            score1 = list(outcomes).index(my_pick) + 1
            total_score += score1 + 6
            print(f"score1: {score1} + 6 = {total_score}")
        elif round[1] == "Y":
            my_pick = outcomes[round[0]][1]
            score1 = list(outcomes).index(my_pick) + 1
            total_score += score1 + 3
            print(f"score1: {score1} + 3 = {total_score}")
        elif round[1] == "X":
            my_pick = outcomes[round[0]][0]
            score1 = list(outcomes).index(my_pick) + 1
            total_score += score1 
            print(f"score1: {score1} + 0 = {total_score}")
        print("-------------------")
    print("Total score: ", total_score)
