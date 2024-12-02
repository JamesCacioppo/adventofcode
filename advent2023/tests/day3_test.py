import day3

def test_each_line_read_from_file(day_three_file):
    assert day_three_file == [
        "467..114..",
        "...*......",
        "..35..633.",
        "......#...",
        "617*......",
        ".....+.58.",
        "..592.....",
        "......755.",
        "...$.*....",
        ".664.598..",
    ]


def test_find_special_chars(day_three_file):
    assert day3.find_special_chars(day_three_file) == [
        (3, 1),
        (6, 3),
        (3, 4),
        (5, 5),
        (3, 8),
        (5, 8),
    ]


def test_build_parts_list(day_three_file):
    parts_list = day3.build_parts_list(day_three_file)
    assert len(parts_list) == 10
    assert parts_list[0].number == 467
    assert parts_list[0].x_min == 0
    assert parts_list[0].x_max == 3
    assert parts_list[0].y == 0

    assert parts_list[1].number == 114
    assert parts_list[1].x_min == 5
    assert parts_list[1].x_max == 8
    assert parts_list[1].y == 0

    assert parts_list[2].number == 35
    assert parts_list[2].x_min == 2
    assert parts_list[2].x_max == 4
    assert parts_list[2].y == 2

    assert parts_list[3].number == 633
    assert parts_list[3].x_min == 6
    assert parts_list[3].x_max == 9
    assert parts_list[3].y == 2

    assert parts_list[4].number == 617
    assert parts_list[4].x_min == 0
    assert parts_list[4].x_max == 3
    assert parts_list[4].y == 4

    assert parts_list[5].number == 58
    assert parts_list[5].x_min == 7
    assert parts_list[5].x_max == 9
    assert parts_list[5].y == 5

    assert parts_list[6].number == 592
    assert parts_list[6].x_min == 2
    assert parts_list[6].x_max == 5
    assert parts_list[6].y == 6

    assert parts_list[7].number == 755
    assert parts_list[7].x_min == 6
    assert parts_list[7].x_max == 9
    assert parts_list[7].y == 7

    assert parts_list[8].number == 664
    assert parts_list[8].x_min == 1
    assert parts_list[8].x_max == 4
    assert parts_list[8].y == 9

    assert parts_list[9].number == 598
    assert parts_list[9].x_min == 5
    assert parts_list[9].x_max == 8
    assert parts_list[9].y == 9


def test_find_search_domain(day_three_file):
    line_length = 10
    part = day3.part(467, 0, 3, 0)
    assert day3.find_search_domain(part, line_length) == [0, 1, 2, 3]
    part = day3.part(114, 5, 8, 0)
    assert day3.find_search_domain(part, line_length) == [4, 5, 6, 7, 8]

    # Let's go through every part in the file
    parts_list = day3.build_parts_list(day_three_file)
    assert day3.find_search_domain(parts_list[0], line_length) == [0, 1, 2, 3]
    assert day3.find_search_domain(parts_list[1], line_length) == [4, 5, 6, 7, 8]
    assert day3.find_search_domain(parts_list[2], line_length) == [1, 2, 3, 4]
    assert day3.find_search_domain(parts_list[3], line_length) == [5, 6, 7, 8, 9]
    assert day3.find_search_domain(parts_list[4], line_length) == [0, 1, 2, 3]
    assert day3.find_search_domain(parts_list[5], line_length) == [6, 7, 8, 9]
    assert day3.find_search_domain(parts_list[6], line_length) == [1, 2, 3, 4, 5]
    assert day3.find_search_domain(parts_list[7], line_length) == [5, 6, 7, 8, 9]
    assert day3.find_search_domain(parts_list[8], line_length) == [0, 1, 2, 3, 4]
    assert day3.find_search_domain(parts_list[9], line_length) == [4, 5, 6, 7, 8]

    # Let's test some cases out of the real data
    line_length = 140
    part = day3.part(445, 13, 16, 133)
    assert day3.find_search_domain(part, line_length) == [12, 13, 14, 15, 16]


def test_find_search_range():
    num_of_lines = 10
    part = day3.part(467, 0, 3, 0)
    assert day3.find_search_range(part, num_of_lines) == [0, 1]
    part = day3.part(114, 5, 8, 0)
    assert day3.find_search_range(part, num_of_lines) == [0, 1]
    # Let's test some cases out of the real data
    num_of_lines = 140
    part = day3.part(445, 13, 16, 133)
    assert day3.find_search_range(part, num_of_lines) == [132, 133, 134]


def test_build_adjacent_position_list():
    assert day3.build_adjacent_position_list(
        part_domain=[0, 1, 2],
        part_y=0,
        special_char_domain=[0, 1, 2, 3],
        special_char_range=[0, 1]
    ) == [(3, 0), (0, 1), (1, 1), (2, 1), (3, 1)]

    assert day3.build_adjacent_position_list(
        part_domain=[2, 3],
        part_y=2,
        special_char_domain=[1, 2, 3, 4],
        special_char_range=[1, 2, 3]
    ) == [(1, 1), (2, 1), (3, 1), (4, 1),
          (1, 2),                 (4, 2),
          (1, 3), (2, 3), (3, 3), (4, 3)]

def test_validate_part(day_three_file):  
    part = day3.part(number=467, x_min=0, x_max=3, y=0)
    special_char_list=day3.find_special_chars(day_three_file)
    day3.validate_part(
        part=part,
        special_char_list=special_char_list,
        adjacent_position_list=[(3, 0), (0, 1), (1, 1), (2, 1), (3, 1)]
    )
    assert part.valid is True

    part = day3.part(number=633, x_min=6, x_max=9, y=2)
    day3.validate_part(
        part=part,
        special_char_list=special_char_list,
        adjacent_position_list=[
            (5, 1), (6, 1), (7, 1), (8, 1), (9, 1),
            (5, 2), (9, 2),
            (5, 3), (6, 3), (7, 3), (8, 3), (9, 3)
            ]
    )
