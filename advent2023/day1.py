import sys
from typing import List, Optional


def read_file(filename) -> list:
    with open(filename, "r") as f:
        lines = f.read().splitlines()
    return lines


def extract_calibration_value(line: str) -> int:
    for i in range(len(line)):
        if line[i].isdigit():
            left_value = line[i]
            break
    for character in reversed(line):
        if character.isdigit():
            right_value = character
            break
    calibration_value_string = left_value + right_value
    calibration_value_int = int(calibration_value_string)
    return calibration_value_int


def sum_calibration_values(calibration_value_list: list[int]) -> int:
    return sum(calibration_value_list)


def convert_word_to_number(word: str) -> int:
    if word in "0123456789":
        return int(word)
    else:
        number_dictionary = {
            "zero": 0,
            "one": 1,
            "two": 2,
            "three": 3,
            "four": 4,
            "five": 5,
            "six": 6,
            "seven": 7,
            "eight": 8,
            "nine": 9,
        }

        return number_dictionary[word.lower()]


def find_first_and_last_numbers(line: str) -> tuple[int, int]:
    number_search_patterns = [
        "0",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]

    # First step is to create a dictionary with the position of the first and last
    # instance of each number in the string.  It will look like:
    # {0: [-1, -1], 1: [-1, -1], 2: [-1, -1], 3: [-1, -1], 4: [-1, -1], 5: [-1, -1], 6: [-1, -1], 7: [-1, -1], 8: [-1, -1], 9: [-1, -1]}
    # where -1 indicates no match.
    matches = {}
    for i in range(10):
        matches[i] = [-1, -1]
    for search_pattern in number_search_patterns:
        matches_dict_key = convert_word_to_number(search_pattern)
        first_hit_location = line.find(search_pattern)
        last_hit_location = line.rfind(search_pattern)
        if first_hit_location != -1:  # If find() returns -1 then do nothing
            if (
                first_hit_location < matches[matches_dict_key][0]
                or matches[matches_dict_key][0] == -1
            ):
                matches[matches_dict_key][0] = first_hit_location
            if last_hit_location > matches[matches_dict_key][1]:
                matches[matches_dict_key][1] = last_hit_location

    # The second step is to determine the very first and last numbers to appear in the string and return those values.
    first_number = 0
    last_number = 0
    for number in matches:
        if matches[first_number][0] == -1:
            first_number = number
        elif matches[number][0] != -1 and matches[number][0] < matches[first_number][0]:
            first_number = number
        if matches[number][1] > matches[last_number][1]:
            last_number = number

    return first_number, last_number


def extract_puz2_calibration_values(left_value: int, right_value: int) -> int:
    return int(str(left_value) + str(right_value))


if __name__ == "__main__":
    lines = read_file(sys.argv[1])

    calibration_value_list = []
    for line in lines:
        calibration_value_list.append(extract_calibration_value(line))

    calibration_value_sum = sum_calibration_values(calibration_value_list)
    print(f"The sum of calibration values for puz 1 is {calibration_value_sum}")

    calibration_value_list.clear()
    for line in lines:
        first, last = find_first_and_last_numbers(line)
        calibration_value_list.append(extract_puz2_calibration_values(first, last))

    print(
        f"The sum of calibration values for puz 2 is {sum_calibration_values(calibration_value_list)}"
    )
