import pytest
from advent2022 import puz1
from pathlib import Path

@pytest.fixture()
def read_file():
  test_file = Path(__file__).parent / "input_test_day1.txt"
  return puz1.read_file(test_file)

def test_each_line_read_from_file(read_file):
  assert read_file == ['1000', '2000', '3000', '', '4000', '', '5000', '6000', '', '7000', '8000', '9000', '', '10000']

def test_calorie_sum_per_elf(read_file):
  elf_sums = puz1.sum_elves(read_file)
  assert elf_sums == [6000, 4000, 11000, 24000, 10000]

def test_find_the_fattest_elf(read_file):
  elf_sums = puz1.sum_elves(read_file)
  fatty = puz1.find_the_fattest_elf(elf_sums)
  assert fatty == 24000
