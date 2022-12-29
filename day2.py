# Getting data
with open("day2.in") as file:
    rounds = [i for i in file.read().strip().split("\n")]

# 9 possible outcomes 

"""
All possible outcomes

Left vs Right | Outcome | Right + outcomes = Total

A vs X = Draw = (1 + 3) = 4
A vs Y = Win = (2 + 6) = 8
A vs Z = Loss = (3 + 0) = 3

B vs X = Loss = (1 + 0) = 1
B vs Y = Draw = (2 + 3) = 5
B vs Z = Win = (3 + 6) = 9

C vs X = Win = (1 + 6) = 7
C vs Y = Loss = (2 + 0) = 2 
C vs Z = Draw = (3 + 3) = 6
"""

outcomes = {
    "A X":4, "A Y":8, "A Z":3,
    "B X":1, "B Y":5, "B Z":9,
    "C X":7, "C Y":2, "C Z":6
}

total_points = 0
for round in rounds:
    total_points += outcomes[round]


print("Answers to part 1: ", total_points)


# Part Two

"""
Y = Draw | X = Lose | Z = Win
"""


strategy_outcomes = {
    "A X":3, "A Y":4, "A Z":8,
    "B X":1, "B Y":5, "B Z":9,
    "C X":2, "C Y":6, "C Z":7
}

strategy_total_points = 0
for round in rounds:
    strategy_total_points += strategy_outcomes[round]

print("Answers to part 2: ", strategy_total_points)