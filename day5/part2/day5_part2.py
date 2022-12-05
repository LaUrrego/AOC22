#                    [L]     [H] [W]
#                [J] [Z] [J] [Q] [Q]
#[S]             [M] [C] [T] [F] [B]
#[P]     [H]     [B] [D] [G] [B] [P]
#[W]     [L] [D] [D] [J] [W] [T] [C]
#[N] [T] [R] [T] [T] [T] [M] [M] [G]
#[J] [S] [Q] [S] [Z] [W] [P] [G] [D]
#[Z] [G] [V] [V] [Q] [M] [L] [N] [R]
# 1   2   3   4   5   6   7   8   9
import re

position_1 = ["Z", "J", "N", "W", "P", "S"]
position_2 = ["G", "S", "T"]
position_3 = ["V", "Q", "R", "L", "H"]
position_4 = ["V", "S", "T", "D"]
position_5 = ["Q", "Z", "T", "D", "B", "M", "J"]
position_6 = ["M", "W", "T", "J", "D", "C", "Z", "L"]
position_7 = ["L", "P", "M", "W", "G", "T", "J"]
position_8 = ["N", "G", "M", "T", "B", "F", "Q", "H"]
position_9 = ["R", "D", "G", "C", "P", "B", "Q", "W"]

group = [
    position_1,
    position_2, 
    position_3, 
    position_4, 
    position_5, 
    position_6, 
    position_7,
    position_8,
    position_9,
    ]

with open ("day5/input/input.txt") as file:
    for line in file:
        #instruction: [how many, from, to]
        instruction = re.findall(r'\d+',line)
        print(instruction)
        how_many = int(instruction[0])
        starting_stack = int(instruction[1]) - 1
        ending_stack = int(instruction[2]) - 1
        for movement in range(-how_many,0):
            moved_crate = group[starting_stack].pop(movement)
            group[ending_stack].append(moved_crate)
        print("current arrangement is:", group)
    print("final look is:", group)
    endings = ""
    for stack in group:
        endings += stack[-1]
    print("End of stacks are: ", endings)