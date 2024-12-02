from advent2024 import day1

def test_each_line_read_from_file(day_one_file):
    assert day_one_file == ["3   4", "4   3", "2   5", "1   3", "3   9", "3   3"]

def test_left_column_list(day_one_file):
    left_column_list, right_column_list = day1.create_left_and_right_lists(day_one_file)
    assert left_column_list == [3, 4, 2, 1, 3, 3]
    assert right_column_list == [4, 3, 5, 3, 9, 3]

def test_sort_list_ascending(day_one_file):
    left_column_list, right_column_list = day1.create_left_and_right_lists(day_one_file)

    ordered_left_column = day1.sort_list_ascending(left_column_list)
    ordered_right_column = day1.sort_list_ascending(right_column_list)

    assert ordered_left_column == [1, 2, 3, 3, 3, 4]
    assert ordered_right_column == [3, 3, 3, 4, 5, 9]

def test_find_distances(day_one_file):
    left_column_list, right_column_list = day1.create_left_and_right_lists(day_one_file)

    ordered_left_column = day1.sort_list_ascending(left_column_list)
    ordered_right_column = day1.sort_list_ascending(right_column_list)

    distances_list = day1.find_distances(ordered_left_column, ordered_right_column)

    assert distances_list == [2, 1, 0, 1, 2, 5]

def test_sum_distances(day_one_file):
    left_column_list, right_column_list = day1.create_left_and_right_lists(day_one_file)

    ordered_left_column = day1.sort_list_ascending(left_column_list)
    ordered_right_column = day1.sort_list_ascending(right_column_list)

    distances_list = day1.find_distances(ordered_left_column, ordered_right_column)

    sum = day1.find_sum_of_distances(distances_list)
    assert sum == 11

def test_get_count():
    list_to_count = [4, 3, 5, 3, 9, 3]

    assert day1.get_count(list_to_count) == {3: 3, 4: 1, 5: 1, 9: 1}

def test_calculate_similarity():
    left_list = [3, 4, 2, 1, 3, 3]
    right_list = [4, 3, 5, 3, 9, 3]

    similarities = day1.calculate_similarity(left_list, right_list)

    assert similarities == [9, 4, 0, 0, 9, 9]