# Read input into a list of strings
# Create two lists of ints, one for each column
# Sort each list in ascending order
# Calc distance (difference) between each left and right element
# Sum distances

import sys
from typing import List
from collections import Counter


def read_file(filename) -> list:
    with open(filename, "r") as f:
        lines = f.read().splitlines()
    return lines

def create_left_and_right_lists(lines: list[str]) -> tuple[list[int], list[int]]:
    left_list = []
    right_list = []

    for line in lines:
        left_list.append(int(line.split()[0]))
        right_list.append(int(line.split()[1]))

    return (left_list, right_list)

def sort_list_ascending(column: list[int]) -> list[int]:
    return sorted(column)

def find_distances(ordered_left_list: list[int], ordered_right_list: list[int]) -> list[int]:
    distance_list = []
    for i in range(len(ordered_left_list)):
        distance_list.append(abs(ordered_left_list[i] - ordered_right_list[i]))
    
    return distance_list

def find_sum_of_distances(distance_list: list[int]) -> int:
    return sum(distance_list)

def get_count(list_to_count: list[int]) -> dict:
    return Counter(list_to_count)

def calculate_similarity(left_list: list[int], right_list: list[int]) -> list[int]:
    right_list_count = get_count(right_list)

    similarities = []
    for location in left_list:
        similarities.append(location * right_list_count[location])

    return similarities

if __name__ == "__main__":
    lines = read_file(sys.argv[1])

    left_list, right_list = create_left_and_right_lists(lines)

    ordered_left_list = sort_list_ascending(left_list)
    ordered_right_list = sort_list_ascending(right_list)

    distance_list = find_distances(ordered_left_list, ordered_right_list)

    total_distance = find_sum_of_distances(distance_list)

    print(f'The total distance is {total_distance}')

    print(f'The similarity score is {sum(calculate_similarity(left_list, right_list))}')