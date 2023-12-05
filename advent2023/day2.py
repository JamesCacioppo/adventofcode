import sys
import day1
import re
from typing import List, Optional

class HandfullOfCubes:
    """
    HandfullOfCubes is an object representing a random handfull of colored
    cubes pulled from a bag.  Cube will be red, green, or blue.

    Attributes:
        num_red (Optional[int]): Number of red cubes
        num_green (Optional[int]): Number of green cubes
        num_blue (Optional[int]): Number of blue cubes

    Methods:
        __init__(self, handfull: str):
            Determine the number of each color of cubes from the handfull string
            argument.
    """
    def __init__(self, handfull: str):
        """
        Initialize the handfull instance.  Determine the number of each color cube
        in the handfull string.

        Args:
            handfull (str): Comma seperated list of cubes (e.g. "1 red, 2 green, 3 blue")
        """
        red = re.search(r'(\d+) red', handfull)
        if red: # we have to test because re.search() will return None if no match
            self.num_red = int(red[1])
        else:
            self.num_red = None
        
        green = re.search(r'(\d+) green', handfull)
        if green:
            self.num_green = int(green[1])
        else:
            self.num_green = None

        blue = re.search(r'(\d+) blue', handfull)
        if blue:
            self.num_blue = int(blue[1])
        else:
            self.num_blue = None

class Game:
    """
    Game class is a record of a singular game.  Each game is multiple handfulls
    of colored cubes.  Cubes can be colored red, green, and blue.

    Attributes:
        game_number (int): A number assigned to each game
        handfull_list (list[handfull_of_cubes]): A list of handfull_of_cubes objects
        required_red (int): Number of required red cubes for a valid game
        required_green (int): Number of required green cubes for a valid game
        required_blue (int): Number of required blue cubes for a valid game
        power (int): Product of the three required quantities

    Methods:
        __init__(self, line_from_file: str):
            Determine game_number from the string argument.  Split the remainder
            of the string into a list of handfulls and create a list of
            HandfullOfCubes objects.

        is_it_a_valid_game(self):
            Determine if it's a valid game by ensuring that none of the handfulls
            exceed the maximum number of possible cubes for any single color.
    """
    def __init__(self, line_from_file: str):
        """
        Initialize the game instance.  Determine the game number from the
        string argument.  Split the remainder of the string and create a
        list of HandfullOfCubes objects.  Find the required number of of cubes
        for each color to be a valid game.  Determine the power of each game
        by taking the product of the the required colors.

        Args:
            line_from_file (str): A string containing all game information (e.g. "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green")
        """
        #parse line and set each value
        self.game_number = int(re.search(r'\d+', line_from_file.split(":")[0])[0])
        handfulls_string = line_from_file.split(":")[1] # A string that looks like "3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
        handfulls_list = handfulls_string.split(";") # A list that looks like [' 3 blue, 4 red', ' 1 red, 2 green, 6 blue', ' 2 green']
        # Create list of handfull_of_cubes
        self.handfull_list = [HandfullOfCubes(handfull) for handfull in handfulls_list]

        self.required_red = 0
        self.required_green = 0
        self.required_blue = 0

        for handfull in self.handfull_list:
            if handfull.num_red is not None and handfull.num_red > self.required_red:
                self.required_red = handfull.num_red
            if handfull.num_green is not None and handfull.num_green > self.required_green:
                self.required_green = handfull.num_green
            if handfull.num_blue is not None and handfull.num_blue > self.required_blue:
                self.required_blue = handfull.num_blue
        
        self.power = self.required_red * self.required_green * self.required_blue
 
    def is_it_a_valid_game(self, max_red: int, max_green: int, max_blue: int) -> bool:
        """
        Determine if a game is valid based on the max number of colored cubes
        provided as arguments.

        Args:
            max_red (int): Maximum number of red cubes in the bag
            max_green (int): Maximum number of green cubes in the bag
            max_blue (int): Maximum number of blue cubes in the bag
        """

        for handfull in self.handfull_list:
            if handfull.num_red and handfull.num_red > max_red:
                return False
            if handfull.num_green and handfull.num_green > max_green:
                return False
            if handfull.num_blue and handfull.num_blue > max_blue:
                return False
        return True


def sum_game_ids(list_of_games: List[Game], max_red: int, max_green: int, max_blue: int) -> int:
    """
    Sum the ID's of valid games in the list argument.

    Args:
        list_of_games (list(Game)): A list of Game objects
    """

    valid_games_id_list = list()
    for game in list_of_games:
        if game.is_it_a_valid_game(max_red=max_red, max_green=max_green, max_blue=max_blue):
            valid_games_id_list.append(game.game_number)
    return sum(valid_games_id_list)

def sum_game_powers(list_of_games: List[Game]):
    sum = 0
    for game in list_of_games:
        sum = sum + game.power

    return sum

if __name__ == '__main__':
    lines = day1.read_file(sys.argv[1])

    list_of_games = list()

    for line in lines:
        list_of_games.append(Game(line))
    
    print(f"The sum of valid game id's is {sum_game_ids(list_of_games, max_red=12, max_green=13, max_blue=14)}")

    print(f"The sum of game powers is {sum_game_powers(list_of_games)}")