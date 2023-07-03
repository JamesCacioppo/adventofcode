import sys

def read_file(filename) -> list:
    with open(filename, 'r') as f:
        lines = f.read().splitlines()
    return(lines)

def sum_elves(lines: list) -> list:
    total = 0
    elf_sums = list()
    number_of_lines = len(lines)
    for i in range(number_of_lines):
        if len(lines[i]) > 0 and i < number_of_lines - 2:
            total += int(lines[i])
        elif len(lines[i]) > 0 and i == number_of_lines -1: # make sure to include the last line if it is non-zero
            total += int(lines[i])
            elf_sums.append(total)
        else:
            elf_sums.append(total)
            total = 0
    return elf_sums

def find_the_fattest_elf(elf_sums: list) -> int:
    elf_sums.sort(reverse=True)
    return elf_sums[0]

def execute():
    lines = read_file('input1.txt')
    elf_sums = sum_elves(lines)
    fatty = find_the_fattest_elf(elf_sums)
    print(f"The fattest elf is carrying {fatty} calories")

if __name__ == '__main__':
    lines = read_file(sys.argv[1])

    elf_sums = sum_elves(lines)

    fatty = find_the_fattest_elf(elf_sums)
    print(f"The fattest elf is carrying {fatty} calories")