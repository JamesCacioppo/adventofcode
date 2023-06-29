# import day2.puz2 as puz2
from advent2022 import puz1
from advent2022 import puz2
import pytest
from pathlib import Path

@pytest.fixture()
def read_file_fixture():
    test_file=Path(__file__).parent / "input_test_day2.txt"
    return puz1.read_file(test_file)

def test_read_file (read_file_fixture):
    assert read_file_fixture == ['A Y', 'B X', 'C Z']

def test_round_class_init_method():
    test_round = puz2.Round('A Y')
    assert test_round.round[0] == 'A'
    assert test_round.round[1] == 'Y'

def test_create_rounds(read_file_fixture):
    play = puz2.create_rounds(read_file_fixture)
    assert play[0].round == ['A', 'Y']
    assert play[1].round == ['B', 'X']
    assert play[2].round == ['C', 'Z']
    assert play[0].false_score == 8
    assert play[1].false_score == 1
    assert play[2].false_score == 6

def test_sum_false_score(read_file_fixture):
    play = puz2.create_rounds(read_file_fixture)
    false_score = puz2.sum_false_score(play)
    assert false_score == 15