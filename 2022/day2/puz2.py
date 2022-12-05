import sys
sys.path.append("..")
from advent2022.day1.puz1 import read_file


class Round:
    shape_value_dict = {
        "rock": 1,
        "paper": 2,
        "scissors": 3
    }

    my_play_dict = {
        "X": "rock",
        "Y": "paper",
        "Z": "scissors"
    }

    opponent_play_dict = {
        "A": "rock",
        "B": "paper",
        "C": "scissors"
    }
    
    result_value_dict = {
        "loss": 0,
        "draw": 3,
        "win": 6
    }

    result_dict = {
        "X": "loss",
        "Y": "draw",
        "Z": "win"
    }

    def __init__(self, line_in_file):
        self.round = line_in_file.split()
        self.false_score = self.calculate_false_score(self.round[0], self.round[1])
        self.true_score = self.calculate_true_score(self.round[0], self.round[1])
        # self.opponent_play = round[0]
        # self.my_false_play = round[1]
        # self.required_round_result = round[1]

    def calculate_false_score(self, opponent_play, my_play):
        my_play_value = self.shape_value_dict[self.my_play_dict[my_play]]
        #determine outcome value
        if self.opponent_play_dict[opponent_play] == self.my_play_dict[my_play]:
            outcome_value = self.result_value_dict["draw"]
        elif self.opponent_play_dict[opponent_play] == "rock":
            if self.my_play_dict[my_play] == "paper": #rock vs paper -> win
                outcome_value = self.result_value_dict["win"]
            elif self.my_play_dict[my_play] == "scissors": #rock vs scissors -> loss
                outcome_value = self.result_value_dict["loss"]
        elif self.opponent_play_dict[opponent_play] == "paper":
            if self.my_play_dict[my_play] == "rock": #paper vs rock -> loss
                outcome_value = self.result_value_dict["loss"]
            elif self.my_play_dict[my_play] == "scissors": #paper vs scissors -> win
                outcome_value = self.result_value_dict["win"]
        elif self.opponent_play_dict[opponent_play] == "scissors":
            if self.my_play_dict[my_play] == "rock": # scissors vs rock -> win
                outcome_value = self.result_value_dict["win"]
            elif self.my_play_dict[my_play] == "paper": #scissors vs paper -> loss
                outcome_value = self.result_value_dict["loss"]

        score = my_play_value + outcome_value
        return score

    def calculate_true_score(self, opponent_play, round_result):
        if self.result_dict[round_result] == "loss":
            if self.opponent_play_dict[opponent_play] == "rock":
                my_play = "scissors"
            elif self.opponent_play_dict[opponent_play] == "paper":
                my_play = "rock"
            elif self.opponent_play_dict[opponent_play] == "scissors":
                my_play = "paper"
        
        elif self.result_dict[round_result] == "draw":
            my_play = self.opponent_play_dict[opponent_play]
        
        elif self.result_dict[round_result] == "win":
            if self.opponent_play_dict[opponent_play] == "rock":
                my_play = "paper"
            elif self.opponent_play_dict[opponent_play] == "paper":
                my_play = "scissors"
            elif self.opponent_play_dict[opponent_play] == "scissors":
                my_play = "rock"

        my_play_value = self.shape_value_dict[my_play]
        score = my_play_value + self.result_value_dict[self.result_dict[round_result]]
        return score

def create_rounds(lines):

    play = list()

    for i in range(len(lines)):
        play.append(Round(lines[i]))

    return play

def sum_false_score(play: list) -> int:
    sum = 0
    for i in range(len(play)):
        sum = sum + play[i].false_score
    return sum

def sum_true_score(play: list) -> int:
    sum = 0
    for i in range(len(play)):
        sum = sum + play[i].true_score
    return sum

def execute(file_name: str):
    lines = read_file(file_name)
    play = create_rounds(lines)
    false_sum = sum_false_score(play)
    true_sum = sum_true_score(play)
    print(f"[*] Day 2: The false total score is {false_sum}")
    print(f"[*] Day 2: The true total score is {true_sum}")

if __name__ == '__main__':
    lines = read_file(sys.argv[1])
    false_sum = sum_false_score(create_rounds(lines))

    print(f"The false total score is {false_sum}")