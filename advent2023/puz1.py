import sys

def read_file(filename) -> list:
    with open(filename, 'r') as f:
        lines = f.read().splitlines()
    return(lines)

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

if __name__ == '__main__':
    lines = read_file(sys.argv[1])

    calibration_value_list = []
    for line in lines:
        calibration_value_list.append(extract_calibration_value(line))

    calibration_value_sum = sum_calibration_values(calibration_value_list)
    print(f'The sum of calibration values is {calibration_value_sum}')