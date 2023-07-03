from advent2022.day1 import puz1
from pathlib import Path

def test_each_line_read_from_file(day_one_file):
  assert day_one_file == ['1000', '2000', '3000', '', '4000', '', '5000', '6000', '', '7000', '8000', '9000', '', '10000']

def test_calorie_sum_per_elf(day_one_file):
  elf_sums = puz1.sum_elves(day_one_file)
  assert elf_sums == [6000, 4000, 11000, 24000, 10000]

def test_find_the_fattest_elf(day_one_file):
  elf_sums = puz1.sum_elves(day_one_file)
  fatty = puz1.find_the_fattest_elf(elf_sums)
  assert fatty == 24000
