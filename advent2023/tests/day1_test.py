from advent2023 import puz1

def test_each_line_read_from_file(day_one_file):
  assert day_one_file == ['1abc2', 'pqr3stu8vwx', 'a1b2c3d4e5f', 'treb7uchet']

def test_get_each_calibration_value(day_one_file):
  assert puz1.extract_calibration_value(day_one_file[0]) == 12
  assert puz1.extract_calibration_value(day_one_file[1]) == 38
  assert puz1.extract_calibration_value(day_one_file[2]) == 15
  assert puz1.extract_calibration_value(day_one_file[3]) == 77

def test_sum_calibration_values(day_one_file):
  calibration_value_list = [12, 38, 15, 77]
  assert puz1.sum_calibration_values(calibration_value_list) == 142

# def test_calorie_sum_per_elf(day_one_file):
#   elf_sums = puz1.sum_elves(day_one_file)
#   assert elf_sums == [6000, 4000, 11000, 24000, 10000]

# def test_find_the_fattest_elf(day_one_file):
#   elf_sums = puz1.sum_elves(day_one_file)
#   fatty = puz1.find_the_fattest_elf(elf_sums)
#   assert fatty == 24000
