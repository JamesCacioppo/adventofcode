from advent2023 import day2

def test_each_line_read_from_file(day_two_puz_one_file):
  assert day_two_puz_one_file == [
    'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
    'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
    'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
    'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
    'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'
  ]

def test_handfull_of_cubes_class():
    game1_handfull0 = day2.HandfullOfCubes('3 blue, 4 red')
    assert game1_handfull0.num_red == 4
    assert game1_handfull0.num_blue == 3
    game1_handfull1 = day2.HandfullOfCubes('1 red, 2 green, 6 blue')
    assert game1_handfull1.num_red == 1
    assert game1_handfull1.num_green == 2
    assert game1_handfull1.num_blue == 6

def test_game_class(day_two_puz_one_file):
    games = list()
    for line in day_two_puz_one_file:
        games.append(day2.Game(line))
    assert len(games) == 5
    for i in range(len(games)):
        assert games[i].game_number == i+1
    assert games[0].handfull_list[0].num_red == 4
    assert games[0].handfull_list[0].num_blue == 3
    assert games[3].handfull_list[1].num_green == 3
    assert games[4].handfull_list[1].num_blue == 2

    assert games[0].required_red == 4
    assert games[0].required_green == 2
    assert games[0].required_blue == 6
    assert games[1].required_red == 1
    assert games[1].required_green == 3
    assert games[1].required_blue == 4
    assert games[2].required_red == 20
    assert games[2].required_green == 13
    assert games[2].required_blue == 6
    assert games[3].required_red == 14
    assert games[3].required_green == 3
    assert games[3].required_blue == 15
    assert games[4].required_red == 6
    assert games[4].required_green == 3
    assert games[4].required_blue == 2

    assert games[0].power == 48
    assert games[1].power == 12
    assert games[2].power == 1560
    assert games[3].power == 630
    assert games[4].power == 36

def test_game_class_is_it_a_valid_game_method(day_two_puz_one_file):
    games = list()
    for line in day_two_puz_one_file:
        games.append(day2.Game(line))
    assert games[0].is_it_a_valid_game(max_red=12, max_green=13, max_blue=14) is True
    assert games[1].is_it_a_valid_game(max_red=12, max_green=13, max_blue=14) is True
    assert games[4].is_it_a_valid_game(max_red=12, max_green=13, max_blue=14) is True
    assert games[2].is_it_a_valid_game(max_red=12, max_green=13, max_blue=14) is False
    assert games[3].is_it_a_valid_game(max_red=12, max_green=13, max_blue=14) is False

def test_sum_game_ids(day_two_puz_one_file):
    games = list()
    for line in day_two_puz_one_file:
        games.append(day2.Game(line))
    assert day2.sum_game_ids(games, 12, 13, 14) == 8

def test_sum_game_powers(day_two_puz_one_file):
    games = list()
    for line in day_two_puz_one_file:
        games.append(day2.Game(line))
    assert day2.sum_game_powers(games) == 2286