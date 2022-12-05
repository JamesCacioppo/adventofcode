from advent2022.day2 import puz2

def test_read_file (day_two_file):
    assert day_two_file == ['A Y', 'B X', 'C Z']

def test_round_class_init_method():
    test_round = puz2.Round('A Y')
    assert test_round.round[0] == 'A'
    assert test_round.round[1] == 'Y'

def test_create_rounds(day_two_file):
    play = puz2.create_rounds(day_two_file)
    assert play[0].round == ['A', 'Y']
    assert play[1].round == ['B', 'X']
    assert play[2].round == ['C', 'Z']
    assert play[0].false_score == 8
    assert play[0].true_score == 4
    assert play[1].false_score == 1
    assert play[1].true_score == 1
    assert play[2].false_score == 6
    assert play[2].true_score == 7

def test_sum_false_score(day_two_file):
    play = puz2.create_rounds(day_two_file)
    false_score = puz2.sum_false_score(play)
    assert false_score == 15

def test_sum_true_score(day_two_file):
    play = puz2.create_rounds(day_two_file)
    true_score = puz2.sum_true_score(play)
    assert true_score == 12