opponentPlay = {
    "a": "rock",
    "b": "paper",
    "c": "scissors"
}

my_play = {
    "x": "rock",
    "y": "paper",
    "z": "scissors"
}

value = {
    "rock": 1,
    "paper": 2,
    "scissors": 3
}

award = {
    "loss": 0,
    "draw": 3,
    "win": 6
}

f = open('input2.txt', 'r')

lines = []

for i in f.readlines():
    lines.append(i)

f.close()

