f = open('test3.txt', 'r')

lines = []

for i in f.readlines():
    lines.append(i)

f.close()

values = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Part 2
num_groups = int(len(lines) / 3)

total_value = 0

for group in range(num_groups):
    print("Group", group)
    elves_in_group = []
    for elf_in_group in range(3):
        elf = 3 * group + elf_in_group
        elves_in_group.append(elf)
    
    print("Elves in group:", elves_in_group)

    for char in lines[elves_in_group[0]]:
        if char in lines[elves_in_group[1]] and char in lines[elves_in_group[2]]:
            badge = char

    print("Badge", badge)
    print("Badge value", values.find(badge) + 1)
    total_value = total_value + values.find(badge) + 1
    print("The total is now", total_value)
        

# Part 1

# total_value = 0

# for j in lines:
#     n = len(j)
#     first_half = j[0:n//2]
#     second_half = j[n//2:n]
#     print(first_half, second_half, end="")

#     duplicate = ""

#     for k in first_half:
#         if k in second_half:
#             duplicate = k
        
#     print("duplicate is", duplicate)

#     total_value = total_value + values.find(duplicate) + 1
#     print("The total is now", total_value)