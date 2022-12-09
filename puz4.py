def createList(r1, r2):
    return list(range(r1, r2+1))

lines = []

with open('input4.txt', 'r') as f:
    for x in f.readlines():
        lines.append(x.strip())
    
# print(lines)

count = 0

for pair in lines:
    # print(pair) # pair is a string
    elf = pair.split(',', 1) # elf is a list of strings
    elf[0] = elf[0].split('-', 1) # elf[0] is now a list of strings which makes elf a list of lists
    elf[1] = elf[1].split('-', 1)

    elf0_rangea = int(elf[0][0])
    elf0_rangeb = int(elf[0][1])
    elf1_rangea = int(elf[1][0])
    elf1_rangeb = int(elf[1][1])

    section_a = createList(elf0_rangea, elf0_rangeb)
    section_b = createList(elf1_rangea, elf1_rangeb)
    print(section_a)
    print(section_b)

    if all(item in section_a for item in section_b):
        print(f"Section a found in section b")
        count += 1
    elif all(item in section_b for item in section_a):
        print(f"Section b found in section a")
        count += 1
    
    print(f"The count is now {count}")