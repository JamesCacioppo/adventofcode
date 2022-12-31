import sys

def read_file(filename):
    with open(filename, 'r') as f:
        lines = f.read().splitlines()
    return lines

def is_tree_visible(lines, x, y):
    x_max = len(lines[y])
    y_max = len(lines)
    row = [tree for tree in lines[y]]
    column = []
    
    for loop_y in range(y_max):
        column.append(lines[loop_y][x])
    
    if x == 0 or x == x_max-1:
        return True
    elif y == 0 or y == y_max-1:
        return True
    # Look left and right
    elif lines[y][x] > max(row[0:x]) or lines[y][x] > max(row[x+1:x_max+1]):
        return True
    # Look up and down
    elif lines[y][x] > max(column[0:y]) or lines[y][x] > max(column[y+1:y_max+1]):
        return True
    else:
        return False

if __name__ == '__main__':
    lines = read_file(sys.argv[1])

    tree_count = 0
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if is_tree_visible(lines, x, y):
                tree_count = tree_count + 1

    print(f'Visible tree count is {tree_count}')