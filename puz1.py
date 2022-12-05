f = open('input1.txt', 'r')

cal_sum = list() # List of each elf's total calories
total = 0

# Calculate each elf's total calories
for x in f.readlines():
  if len(x) > 1:
    total += int(x)
  else:
    cal_sum.append(total)
    total = 0

fatty = 0 # Number of the fattest elf

for i in range(0, len(cal_sum)-1):
  if cal_sum[i] > cal_sum[fatty]:
    fatty = i
  elif cal_sum[i] == cal_sum[fatty] and i != 0:
    print("We have a tie between elf", fatty, "and elf", i)

print("The fattest elf is number", fatty)
print("The fat elf is carrying", cal_sum[fatty], "calories. Fat is a way of life!")

# Sort the list of total calories
cal_sum.sort(reverse=True)
del cal_sum[3:]
fat_three_total = 0

for i in cal_sum:
  fat_three_total += i

print("The fattest three elves are carrying", fat_three_total, "calories total.")

f.close()
