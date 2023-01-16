with open("day4.in") as file:
    sections = [i for i in file.read().strip().split("\n")]

pairs = 0
for assignemnts in sections:
    first, second = assignemnts.split(",")

    first = [int(i) for i in first.split("-")]
    second = [int(i) for i in second.split("-")]

    if first[0] <= second[0] and first[1] >= second[1]: pairs += 1
    elif second[0] <= first[0] and second[1] >= first[1]: pairs += 1

print("Part 1: ", pairs)

pairs = 0
for assignemnts in sections:
    first, second = assignemnts.split(",")

    first = [int(i) for i in first.split("-")]
    second = [int(i) for i in second.split("-")]

    if first[0] is range(second[0], second[1]+1) or first[1] in range(second[0], second[1]+1): pairs += 1
    elif second[0] is range(first[0], first[1]+1) or second[1] in range(first[0], first[1]+1): pairs += 1
    
print("Part 2: ", pairs)