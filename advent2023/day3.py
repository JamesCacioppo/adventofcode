import copy
import re
import sys
from day1 import read_file


class part:
    def __init__(self, number: int, x_min: int, x_max: int, y: int):
        self.number = number
        self.x_min = x_min
        self.x_max = x_max
        self.y = y
        self.valid = False

def find_special_chars(lines: list[str]) -> list[tuple[int, int]]:
    """
    Find all special chars and create a list of x,y coordinates of their
    locations.

    Args:
        lines (list(str)): List of lines containing alphanum and special chars
    """
    special_char_list = list()
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if lines[y][x].isalnum() is False and lines[y][x] != ".":
                special_char_list.append((x, y))
    return special_char_list


def build_parts_list(lines: list[str]) -> list[part]:
    """
    Get every number in a list of strings and and create a list of part objects.
    """
    parts_list = list()
    for y in range(len(lines)):
        line = lines[y]
        matches = re.findall(r"\d+", line)
        for match in matches:
            x_min = re.search(match, line).start()
            x_max = re.search(match, line).end()
            parts_list.append(part(int(match), x_min, x_max, y))
    return parts_list


def validate_part(
    part: part,
    special_char_list: list[tuple[int, int]],
    adjacent_position_list: list[tuple[int, int]]
):
    """
    Determine if a provided part is valid or not.

    Args:
        part (part): A list of part objects
        special_char_list (list(tuple(int, int))): A list of x,y coordinates of special chars
        adjacent_position_list (list(tuple(int, int))): A list of x,y coordinates of positions adjacent to the part
    """

    for position in adjacent_position_list:
        if position in special_char_list:
            part.valid = True
            break


def find_search_domain(part: part, line_length: int) -> list[int]:
    # Find domain of possible special char locations. Domain of special chars is domain of part +/- 1.
    part_domain = list(range(part.x_min, part.x_max))
    special_char_domain = copy.deepcopy(part_domain)
    if part.x_max != line_length:
        special_char_domain.append(special_char_domain[-1] + 1)
    if part.x_min != 0:
        special_char_domain.insert(0, special_char_domain[0] - 1)
    return special_char_domain


def find_search_range(part: part, num_of_lines: int) -> list[int]:
    # Find possible range of special char locations
    special_char_range = [part.y]
    if part.y > 0:
        special_char_range.insert(0, part.y - 1)
    if part.y < num_of_lines - 1:
        special_char_range.append(part.y + 1)
    return special_char_range


def build_adjacent_position_list(
    part_domain: list[int],
    part_y: int,
    special_char_domain: list[int],
    special_char_range: list[int]
) -> list[tuple[int, int]]:
    """
    Build a list of tuples representing coordinates of positions adjacent to a
    part that could hold a special character.

    Args:
        part_domain (list(int))
        special_char_domain (list(int))
        special_char_range (list(int))
    """
    # Create a list[tuple[int, int]] of adjacent positions to search.
    adjacent_position_list = list()
    for y in special_char_range:
        for x in special_char_domain:
            if not (x in part_domain and y == part_y):
                adjacent_position_list.append((x, y))
    return adjacent_position_list


def sum_part_numbers(parts_list: list[part]) -> int:
    total = 0
    for part in parts_list:
        if part.valid is True:
            total = total + part.number
    return total


if __name__ == "__main__":
    lines = read_file(sys.argv[1])

    # Iterate through and create a list of the locations of any special character
    special_char_list = find_special_chars(lines)

    # Create an object for each number and its coordinates.
    parts_list = build_parts_list(lines)

    line_length = len(lines[0])
    num_of_lines = len(lines)
    for the_part in parts_list:
        adjacent_position_list = build_adjacent_position_list(
            part_domain=list(range(the_part.x_min, the_part.x_max)),
            part_y=the_part.y,
            special_char_domain=find_search_domain(the_part, line_length),
            special_char_range=find_search_range(the_part, num_of_lines)
        )

        validate_part(part=the_part, special_char_list=special_char_list, adjacent_position_list=adjacent_position_list)
    
    print(f'The total of the valid parts is {sum_part_numbers(parts_list=parts_list)}')