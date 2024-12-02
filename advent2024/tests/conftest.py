from pathlib import Path
import pytest
from advent2024 import day1


@pytest.fixture()
def day_one_file():
    test_file = Path(__file__).parent / "input_test_day1.txt"
    return day1.read_file(test_file)