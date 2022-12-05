from advent2022.day8 import puz8

def test_tree_class(day_eight_file):
    first_tree = puz8.Tree(3)
    assert first_tree.height == 3

