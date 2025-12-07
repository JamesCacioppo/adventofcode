import pytest

from day1 import part1, part2, read_file, is_rotation_zero


def test_read_file():
    lines = read_file("data/day1_test_input.txt")
    assert lines == [
        "L68",
        "L30",
        "R48",
        "L5",
        "R60",
        "L55",
        "L1",
        "L99",
        "R14",
        "L82"
    ]