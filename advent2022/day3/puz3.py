import sys
sys.path.append("..")
from advent2022.day1.puz1 import read_file

class Rucksack:
    def __init__(self, line_in_file):
        self.rucksack = line_in_file
        split = int(len(line_in_file)/2)
        self.compartment = [line_in_file[:split], line_in_file[split:]] # this results in a list of strings.

        for i in self.compartment[0]:
            if i in self.compartment[1]:
                self.duplicate_item = i

        values = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

        self.priority = values.find(self.duplicate_item) + 1

def total_priority(rucksack: list) -> int:
    """ Take a list of rucksack objects and return the sum of priorities """
    total_priority = 0
    for i in rucksack:
        total_priority = i.priority + total_priority
    return total_priority

def group_elves_together(group_number: int) -> list:
    """ Take in the group number an return a list of elf numbers in that group """
    list_of_elves_in_group = list()
    for elf_in_group in range(3):
        elf = 3 * group_number + elf_in_group
        list_of_elves_in_group.append(elf)
    return list_of_elves_in_group

def find_badge(all_rucksacks: list, group: int) -> str:
    """Takes in a list of rucksack objects and a list of indexes representing groups of three elves.  Returns the character that all three rucksacks in the group have in common."""
    list_of_elves_in_group = group_elves_together(group)
    rucksack = list()
    for i in list_of_elves_in_group:
        rucksack.append(all_rucksacks[i])

    for i in rucksack[0].rucksack:
        if i in rucksack[1].rucksack and i in rucksack[2].rucksack:
            return i
        
def find_priority(badge: str) -> int:
    """Take in a single character and return it's value"""
    values = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    priority = values.find(badge) + 1
    return priority

if __name__ == '__main__':
    lines = read_file(sys.argv[1])

    # Create a list of Rucksack objects
    all_rucksacks = list()
    for i in lines:
        all_rucksacks.append(Rucksack(i))

    print(f"The total priority is: {total_priority(all_rucksacks)}")

    # Here's how we're going to do this.  We'll operate on groups of 3 elves
    # Step 1: Create groups of 3 elves. This is a list of the elf numbers.
    # Step 2: Determine the badge type. This will be the char that exists in all three rucksacks.
    # Step 3: Sum the new priority of all badges.

    if len(lines) % 3 == 0: # Check to make sure the input is evenly divisible by 3
        num_groups = int(len(lines) / 3)
        
        badge_priority_sum = 0
        for group_number in range(num_groups):
            group_badge = find_badge(all_rucksacks, group_number)
            badge_priority_sum = badge_priority_sum + find_priority(group_badge)

        print(f"The sum of badge priorities is {badge_priority_sum}")
    else:
        print(f"The number of elves provided was not evenly divisible by 3.")

    