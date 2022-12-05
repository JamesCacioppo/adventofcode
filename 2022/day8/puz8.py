import sys
sys.path.append("..")
from advent2022.day1.puz1 import read_file

class Tree:
    def __init__(self, height):
        self.height: int = height

    def add_left_node(self, left_node: Tree):
        self.left_node = left_node

    def add_right_node(self, right_node: Tree):
        self.right_node = right_node
        
def create_forest(lines):
    

if __name__ == "__main__":
    lines = read_file(sys.argv[1])