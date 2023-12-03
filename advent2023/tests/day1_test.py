from advent2023 import day1

def test_each_line_read_from_file(day_one_file):
  assert day_one_file == ['1abc2', 'pqr3stu8vwx', 'a1b2c3d4e5f', 'treb7uchet']

def test_get_each_calibration_value(day_one_file):
  assert day1.extract_calibration_value(day_one_file[0]) == 12
  assert day1.extract_calibration_value(day_one_file[1]) == 38
  assert day1.extract_calibration_value(day_one_file[2]) == 15
  assert day1.extract_calibration_value(day_one_file[3]) == 77

def test_sum_calibration_values():
  calibration_value_list = [12, 38, 15, 77]
  assert day1.sum_calibration_values(calibration_value_list) == 142

def test_each_line_read_from_file_two(day_one_two_file):
  assert day_one_two_file == ['two1nine', 'eightwothree', 'abcone2threexyz', 'xtwone3four', '4nineeightseven2', 'zoneight234', '7pqrstsixteen', 'abc123oneight']

def test_extract_puz2_calibration_values():
  assert day1.extract_puz2_calibration_values(2, 9) == 29
  assert day1.extract_puz2_calibration_values(8, 3) == 83
  assert day1.extract_puz2_calibration_values(1, 3) == 13
  assert day1.extract_puz2_calibration_values(2, 4) == 24
  assert day1.extract_puz2_calibration_values(4, 2) == 42
  assert day1.extract_puz2_calibration_values(1, 4) == 14
  assert day1.extract_puz2_calibration_values(7, 6) == 76

def test_sum_calibration_values_from_puz2():
  calibration_value_list = [29, 83, 13, 24, 42, 14, 76]
  assert day1.sum_calibration_values(calibration_value_list) == 281

def test_convert_word_to_number():
  assert day1.convert_word_to_number('one') == 1
  assert day1.convert_word_to_number('two') == 2
  assert day1.convert_word_to_number('three') == 3
  assert day1.convert_word_to_number('four') == 4
  assert day1.convert_word_to_number('five') == 5
  assert day1.convert_word_to_number('six') == 6
  assert day1.convert_word_to_number('seven') == 7
  assert day1.convert_word_to_number('eight') == 8
  assert day1.convert_word_to_number('nine') == 9
  assert day1.convert_word_to_number('1') == 1
  assert day1.convert_word_to_number('2') == 2

def test_find_first_and_last_numbers(day_one_two_file):
  assert day1.find_first_and_last_numbers(day_one_two_file[0]) == (2, 9)
  assert day1.find_first_and_last_numbers(day_one_two_file[1]) == (8, 3)
  assert day1.find_first_and_last_numbers(day_one_two_file[2]) == (1, 3)
  assert day1.find_first_and_last_numbers(day_one_two_file[3]) == (2, 4)
  assert day1.find_first_and_last_numbers(day_one_two_file[4]) == (4, 2)
  assert day1.find_first_and_last_numbers(day_one_two_file[5]) == (1, 4)
  assert day1.find_first_and_last_numbers(day_one_two_file[6]) == (7, 6)
  assert day1.find_first_and_last_numbers(day_one_two_file[7]) == (1, 8) #An interesting edge case not included in the provided tests
