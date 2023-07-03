from pathlib import Path
import pytest
from advent2022.day1 import puz1

@pytest.fixture()
def day_one_file():
    test_file=Path(__file__).parent / "input_test_day1.txt"
    return puz1.read_file(test_file)

@pytest.fixture()
def day_two_file():
    test_file=Path(__file__).parent / "input_test_day2.txt"
    return puz1.read_file(test_file)