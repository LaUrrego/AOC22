#A rock, B paper, C scissor
#X rock, Y paper, Z scissor
#score: 1 rock, 2 paper, 3 scissor + 0 lose, 3 draw, 6 win
outcomes = {
        "X": ["B", "A", "C"],
        "Y": ["C", "B", "A"],
        "Z": ["A", "C", "B"] 
    }
with open("./input/input.txt") as file:
    total_score = 0
    for line in file:
        round = line.strip().split(" ")
        print("round:", round)
        score1 = list(outcomes).index(round[1]) + 1
        print("score1:", score1)
        score2 = outcomes[round[1]].index(round[0]) * 3
        print("score2:", score2)
        combined_score = score1 + score2
        print("combined score:", combined_score)
        total_score += combined_score
        print("total score:", total_score)
        print("---------")
print("total score = ", total_score)