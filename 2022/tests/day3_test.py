from advent2022.day3 import puz3

def build_rucksack(file) -> list:
    """Take a list of lines in a file. Return list of rucksack objects"""
    rucksack = list()

    for i in range(len(file)):
        rucksack.append(puz3.Rucksack(file[i]))

    return rucksack

def test_read_file(day_three_file):
    assert day_three_file == ['vJrwpWtwJgWrhcsFMMfFFhFp', 'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL', 'PmmdzqPrVvPwwTWBwg', 'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn','ttgJtRGJQctTZtZT', 'CrZsJsPPZsGzwwsLwLmpwMDw']

def test_rucksack_class(day_three_file):
    rucksack = build_rucksack(day_three_file)
    
    assert rucksack[0].compartment == ['vJrwpWtwJgWr', 'hcsFMMfFFhFp']
    assert rucksack[1].compartment == ['jqHRNqRjqzjGDLGL', 'rsFMfFZSrLrFZsSL']
    assert rucksack[2].compartment == ['PmmdzqPrV', 'vPwwTWBwg']

    assert rucksack[0].duplicate_item == 'p'
    assert rucksack[1].duplicate_item == 'L'
    assert rucksack[2].duplicate_item == 'P'
    assert rucksack[3].duplicate_item == 'v'
    assert rucksack[4].duplicate_item == 't'
    assert rucksack[5].duplicate_item == 's'

    assert rucksack[0].priority == 16
    assert rucksack[1].priority == 38
    assert rucksack[2].priority == 42
    assert rucksack[3].priority == 22
    assert rucksack[4].priority == 20
    assert rucksack[5].priority == 19

def test_total_priority(day_three_file):
    rucksack = build_rucksack(day_three_file)
    assert puz3.total_priority(rucksack) == 157

def test_group_elves_together(day_three_file):
    rucksack = build_rucksack(day_three_file)

    assert puz3.group_elves_together(0) == [0, 1, 2]
    assert puz3.group_elves_together(1) == [3, 4, 5]

def test_find_badge(day_three_file):
    rucksack = build_rucksack(day_three_file)

    assert puz3.find_badge(rucksack, 0) == 'r'
    assert puz3.find_badge(rucksack, 1) == 'Z'

def test_find_priority():
    assert puz3.find_priority('a') == 1
    assert puz3.find_priority('p') == 16