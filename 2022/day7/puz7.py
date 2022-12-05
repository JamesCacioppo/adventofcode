import sys

class Node:
    def __init__(self, name, parent=None, size=0):
        self.name = name
        self.size = size
        self.parent = parent
        self.children = []
        if size == 0:
            self.is_file = False
        else:
            self.is_file = True

    def __repr__(self):
        return('My name is ' + self.name)

    
    def find(self, target):
        for child in self.children:
            if child.name == target:
                return(child)

def read_file(filename):
    with open(filename, 'r') as f:
        lines = f.read().splitlines()
    return(lines)

def move(root):
    global dir_less_than_size_list
    if len(root.children) == 0:
        return
    else:
        for i in root.children:
            move(i)
        if root.name != "root":
            root.parent.size = root.parent.size + root.size
        print(f'dir {root.name} size is {root.size}')
        dir_size_list.append(root.size)
        if root.size <= 100000:
            dir_less_than_size_list.append(root.size)
        return

def find_smallest_value_greater_than(size_list, minimum_size):
    for i in size_list:
        if i >= minimum_size:
            return i
    print(f'no dir gt {minimum_size} exists in list')

if __name__ == '__main__':
    lines = read_file(sys.argv[1])

    tree = Node("root")
    root = tree

    for line in lines:
        if line.split()[1] == "cd":
            target = line.split()[2]
            if target == "/":
                tree = root
            elif target == "..":
                tree = tree.parent
            else:
                tree = tree.find(target)

        elif line.split()[1] == "ls":
            print(f'this command is ls')

        elif line.split()[0] == "dir":
            # dir a
            dir_name = line.split()[1]
            tree.children.append(Node(dir_name, tree))

        else:
            # 14848514 b.txt
            size, file_name = line.split()
            size = int(size)
            print(f'{file_name} is a file of {size} bytes')
            tree.children.append(Node(file_name, tree, size))
            tree.size = tree.size + size
            print(f"total size of {tree.name} is now {tree.size}")
    
    dir_less_than_size_list = []
    dir_size_list = []
    move(root)
    print(f'------------- Dirs less than 10,000 --------------')
    print(dir_less_than_size_list)
    print(sum(dir_less_than_size_list))
    print(f"------------- All dirs -------------")
    print(dir_size_list)

    total_disk_size = 70000000
    free_space_needed = 30000000
    print(f'total disk size is {total_disk_size}')
    print(f'free space needed is {free_space_needed}')
    print(f'root size is {root.size}')
    current_free_space = total_disk_size - root.size
    print(f'current free space is {current_free_space}')
    print(f'we need to free up {free_space_needed - current_free_space}')
    
    dir_size_list.sort(reverse=False)
    print(dir_size_list)

    print(find_smallest_value_greater_than(dir_size_list, free_space_needed - current_free_space))