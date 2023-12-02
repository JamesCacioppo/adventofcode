opp_play = {
    "A": "rock",
    "B": "paper",
    "C": "scissors"
}

shape_value = {
    "rock": 1,
    "paper": 2,
    "scissors": 3
}

result = {
    "X": "lose",
    "Y": "draw",
    "Z": "win"
}

result_value = {
    "loss": 0,
    "draw": 3,
    "win": 6
}

f = open('input2.txt', 'r')

lines = []

for i in f.readlines():
    lines.append(i)

f.close()

total_score = 0

for i in lines:
    round = i.split()
    print("Opponent played", round[0], "which is", opp_play[round[0]])
    print("You need to", round[1], "which is", result[round[1]])

    # Determine win/loss
    if round[0] == "A": # Rock
        match round[1]:
            case "X": # Lose
                play = "scissors"
            case "Y": # Draw
                play = "rock"
            case "Z": # Win
                play = "paper"

    elif round[0] == "B": # Paper
        match round[1]:
            case "X": # Lose
                play = "rock"
            case "Y": # Draw
                play = "paper"
            case "Z": # Win
                play = "scissors"

    elif round[0] == "C": # Scissors
        match round[1]:
            case "X": # Lose
                play = "paper"
            case "Y": # Draw
                play = "scissors"
            case "Z": # Win
                play = "rock"

    print("You need to play", play)

    sub_score = 0

    match round[1]:
        case "Z":
            sub_score += 6
            print(sub_score, "points were awarded for a", result["Z"])
        case "Y":
            sub_score += 3
            print(sub_score, "points were awarded for a", result["Y"])
        case "X":
            print("No points were awarded for a", result["X"])

    sub_score += shape_value[play]
    print(shape_value[play], "points awarded for", play)
    print("sub_score is ", sub_score, "for this round.")
    
    total_score += sub_score
    print("The total score is now", total_score)
    print()