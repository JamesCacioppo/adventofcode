from pathlib import Path
import pytest
from advent2023 import puz1

@pytest.fixture()
def day_one_file():
    test_file=Path(__file__).parent / "input_test_day1.txt"
    return puz1.read_file(test_file)
