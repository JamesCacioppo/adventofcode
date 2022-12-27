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

    # def update_size(self, root):
    #     """
    #     Post order traversal to update dir sizes.
    #     """

    #     if root:
    #         sizes = []
    #         for child in self.children:
    #             if not child.is_file:
    #                 root.update_size(child)
    #                 print(child.name)
    
    def find(self, target):
        for child in self.children:
            if child.name == target:
                return(child)

def read_file(filename):
    with open(filename, 'r') as f:
        lines = f.read().splitlines()
    return(lines)

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

    # root.update_size(root)