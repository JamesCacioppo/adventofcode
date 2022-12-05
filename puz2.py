opponent_play = {
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

for i in lines:
    round = i.split()
    print("0 is", round[0])
    print("1 is", round[1])

    # Determine win/loss for a
    if round[0] == "a": # Rock
        print("Opponent played rock")

        match round[1]:
            case "X": # Rock
                result = "draw"
            case "Y": # Paper
                result = "win"
            case "Z": # Scissors
                result = "loss"
    elif round[0] == "B": # Paper
        print("Opponent played paper")