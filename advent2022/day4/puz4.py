import sys
sys.path.append("..")
from advent2022.day1.puz1 import read_file

class ElfPair:
    def __init__(self, line: str):
        self.elf_pair_assigned_sections = line.split(",")

        elf_a_range = self.elf_pair_assigned_sections[0].split('-')
        elf_b_range = self.elf_pair_assigned_sections[1].split('-')

        self.elf_a_assigned_sections = list(range(int(elf_a_range[0]), int(elf_a_range[1]) + 1))
        self.elf_b_assigned_sections = list(range(int(elf_b_range[0]), int(elf_b_range[1]) + 1))


if __name__ == "__main__":
    # Read in the file specified as a command line arg and create a list of ElfPair objects
    lines = read_file(sys.argv[1])
    elf_pairs = list()
    for line in lines:
        elf_pairs.append(ElfPair(line))

    # Determine in how many pairs of elves one assignment fully contains another.
    all_in_count = 0
    for elf_pair in elf_pairs:
        if all(item in elf_pair.elf_a_assigned_sections for item in elf_pair.elf_b_assigned_sections):
            all_in_count += 1
        elif all(item in elf_pair.elf_b_assigned_sections for item in elf_pair.elf_a_assigned_sections):
            all_in_count += 1

    print(f"The all in count is: {all_in_count}")

    # Determine how many pairs of elves have overlapping assignments
    any_in_count = 0
    for elf_pair in elf_pairs:
        if any(item in elf_pair.elf_a_assigned_sections for item in elf_pair.elf_b_assigned_sections):
            any_in_count += 1

    print(f"The any in count is: {any_in_count}")