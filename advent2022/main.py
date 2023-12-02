import sys
from day1.puz1 import execute as day_one_execute
from day2.puz2 import execute as day_two_execute
from day3.puz3 import execute as day_three_execute


if __name__ == '__main__':
    day_one_execute('data/day_1_input.txt')
    day_two_execute('data/day_2_input.txt')
    day_three_execute('data/day_2_input.txt')