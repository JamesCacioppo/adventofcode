# read in file one line at a time
# check for empty line
# if not empty line && empty line count = 0 -> append to crates[]
# elif not empty line && empty line count > 0 -> append to moves[]
# else -. empty line count = 1

def open_file(file_name):
    crates = []
    moves = []
    empty_line = 0
    with open(file_name, 'r') as f:
        for x in f.readlines():
            if x.strip() and empty_line == 0: # x.strip is true if there's something other than white space and line returns
                crates.append(x.strip("\n"))
            elif x.strip() and empty_line > 0:
                moves.append(x.strip())
            else:
                empty_line = 1
    return(crates, moves)

def find_number_of_stacks(crates):
    """
    Take a list of strings and return a count of columns.
    Columns are counted by removing all whitespace from the last row which must
    contain only the numbers of each column.
    """
    number_row = len(crates) -1
    number_of_columns = len(crates[number_row].replace(" ", ""))
    return number_of_columns

def determine_move(move):
    """Accept a string and return a list with the integer parts of the string"""
    move_list = move.split()
    return([int(move_list[1]), int(move_list[3]), int(move_list[5])])

def reorg_crates(crates, number_of_columns):
    new_crates = []
    number_of_rows = len(crates)
    for i in range(number_of_rows - 1): # iterate in -y direction
        new_crates.append([])
        for j in range(number_of_columns + 1): # iterate in x direction
            if j == 1:
                new_crates[i].append(crates[i][1])
            elif j > 1:
                new_crates[i].append(crates[i][1 + ((j - 1) * 4)])
    return(new_crates)

def reorg_stack_as_list(new_crates, number_of_columns):
    number_of_rows = len(new_crates)
    print(f"rows: {number_of_rows}")
    print(f"cols: {number_of_columns}")
    new_stacks = []
    for y in range(number_of_columns):
        stack = []
        for x in range(number_of_rows):
            if new_crates[x][y].strip():
                stack.insert(0, new_crates[x][y])
        new_stacks.append(stack)
    return(new_stacks)

def find_tops(new_stacks):
    tops = ""
    for i in range(len(new_stacks)):
        tops = tops + new_stacks[i][-1]
    return(tops)

crates, moves = open_file("input5.txt")

number_of_columns = find_number_of_stacks(crates)
new_crates = reorg_crates(crates, number_of_columns)

new_stacks = reorg_stack_as_list(new_crates, number_of_columns)

    # Now move the crates
for i in range(len(moves)):
    short_moves = determine_move(moves[i])
    insert_position = len(new_stacks[short_moves[2] - 1])
    for j in range(short_moves[0]):
        new_stacks[short_moves[2] - 1].insert(insert_position, new_stacks[short_moves[1] - 1][-1])
        new_stacks[short_moves[1] - 1].pop(-1)

print(f"The tops are {find_tops(new_stacks)}")