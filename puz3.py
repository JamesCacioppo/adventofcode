f = open('input3.txt', 'r')

lines = []

for i in f.readlines():
    lines.append(i)

f.close()

values = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

total_value = 0

for j in lines:
    n = len(j)
    first_half = j[0:n//2]
    second_half = j[n//2:n]
    print(first_half, second_half, end="")

    duplicate = ""

    for k in first_half:
        if k in second_half:
            duplicate = k
        
    print("duplicate is", duplicate)

    total_value = total_value + values.find(duplicate) + 1
    print("The total is now", total_value)