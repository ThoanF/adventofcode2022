# Taking input file and putting in list
with open('day1.in') as file:
    data = [i for i in file.read().strip().split("\n")]


# Traversing every string in data
max = 0    # Elf with most
max2 = 0   # Elf with second most 
max3 = 0   # Elf with third most
count = 0
for item in data:
    if item == '':
        count = 0  # Resetting the count
    else:
        num = int(item)
        count += num
    
    if count > max:
        max = count
    elif count > max2:
        max2 = count
    elif count > max3:
        max3 = count

print("Answer to part 1:", max)
print("Answer to part 2:", max + max2 + max3)

# Part 2 isn't working; not sure why