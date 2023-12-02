import sys

class Grid:
    def __init__(self, lines):
        self.x_max = len(lines[0])
        self.y_max = len(lines)
        self.trees = [[Tree(x_pos, y_pos, lines[y_pos][x_pos]) for x_pos in range(self.x_max)] for y_pos in range(self.y_max)] #use list comprehension to generate grid list

    def debug(self):
        for y_pos in range(self.y_max):
            for x_pos in range(self.x_max):
                self.trees[y_pos][x_pos].scenic_score = x_pos + y_pos
                print(f'calc_scores is now on ({x_pos},{y_pos})')
                sub_x_pos, sub_y_pos, sub_scenic_score, sub_height = self.trees[y_pos][x_pos].debug()
                print(f"Tree ({sub_x_pos},{sub_y_pos}) has a height of {sub_height} and a scenic score of {sub_scenic_score}")
        return "Method calc_scores is complete!"

class Tree:
    def __init__(self, x_pos, y_pos, height):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.height = height
        self.scenic_score = 0

    def debug(self):
        return self.x_pos, self.y_pos, self.scenic_score, self.height

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

def calc_score(list, grid, ascending):
    score = 0
    if ascending:
        
    else:

    return score

def calc_scenic_score(grid):
    best_score = 0
    for y_pos in range(grid.y_max):
        for x_pos in range(grid.x_max):
            # Here we work on each tree
            if x_pos != 0:
                left_list = range(x_pos)
            else:
                left_list = None
            score = calc_score(left_list, grid, ascending=False) 

            if x_pos != grid.x_max - 1:
                right_list = range(x_pos + 1, grid.x_max)
            else:
                right_list = None
            score = score + calc_score(right_list, grid)

            if y_pos != 0:
                up_list = range(y_pos)
            else:
                up_list = None
            score = score + calc_score(up_list, grid)

            if y_pos != grid.y_max -1:
                down_list = range(y_pos +1, grid.y_max)
            else:
                down_list = None
            score = score + calc_score(down_list, grid)

            print(f'({x_pos},{y_pos}) left_list = {left_list} and right_list = {right_list}')

    return best_score                 

if __name__ == '__main__':
    lines = read_file(sys.argv[1])

    tree_count = 0
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if is_tree_visible(lines, x, y):
                tree_count = tree_count + 1

    print(f'Visible tree count is {tree_count}')

    forest_grid = Grid(lines)
    print(forest_grid.debug())

    best_score = calc_scenic_score(forest_grid)
    print(f'The highest scenic score is {best_score}')