# "A": "rock",
# "B": "paper",
# "C": "scissors",
# "X": "rock",
# "Y": "paper",
# "Z": "scissors"
# "rock": 1,
# "paper": 2,
# "scissors": 3,
# "loss": 0,
# "draw": 3,
# "win": 6

f = open('input2.txt', 'r')

lines = []

for i in f.readlines():
    lines.append(i)

f.close()

total_score = 0

for i in lines:
    round = i.split()
    print("Opponent played", round[0])
    print("You play", round[1])

    # Determine win/loss
    if round[0] == "A": # Rock
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

        match round[1]:
            case "X": # Rock
                result = "loss"
            case "Y": # Paper
                result = "draw"
            case "Z": # Scissors
                result = "win"

    elif round[0] == "C": # Scissors
        print("Opponent played Scissors")

        match round[1]:
            case "X": # Rock
                result = "win"
            case "Y": # Paper
                result = "loss"
            case "Z": # Scissors
                result = "draw"

    print("The result is a", result)

    sub_score = 0

    match result:
        case "win":
            sub_score += 6
            print(sub_score, "points were awarded for a", result)
        case "draw":
            sub_score += 3
            print(sub_score, "points were awarded for a", result)
        case "loss":
            print("No points were awarded for a", result)
    
    match round[1]:
        case "X":
            sub_score += 1
            print("1 point was awarded for Rock")
            print("sub_score is now", sub_score)
        case "Y":
            sub_score += 2
            print("2 points were awarded for Paper")
            print("sub_score is now", sub_score)
        case "Z":
            sub_score += 3
            print("3 points were awarded for Scissors")
            print("sub_score is now", sub_score)
    
    total_score += sub_score

print("The total score:", total_score)