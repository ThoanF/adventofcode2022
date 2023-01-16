from string import ascii_letters

# Gettting data
with open("day3.in") as file:
    compartments = [i for i in file.read().strip().split("\n")]

totalSum = 0

# Iterate through the data
for rucksack in compartments:
    # Two compartments
    half = len(rucksack)//2

    left = set(rucksack[:half])
    right = set(rucksack[half:])

    for priority, char in enumerate(ascii_letters):
        if char in left and char in right:
            totalSum += priority + 1


print("Part 1: ", totalSum)

totalSumP2 = 0
j = 3
for i in range(0, len(compartments), 3):
    rucksacks = compartments[i:j]
    j += 3

    for priority, char in enumerate(ascii_letters):
        if char in rucksacks[0] and char in rucksacks[1] and char in rucksacks[2]:
            totalSumP2 += priority + 1

print("Part 2: ", totalSumP2)