rounds = []
with open("input.txt") as f:
    for line in f:
        rounds.append(line.strip().replace(" ", ""))
scoring_map = {
    "AX": 4,  # draw
    "BX": 1,  # lost
    "CX": 7,  # won
    "AY": 8,  # won
    "BY": 5,  # draw
    "CY": 2,  # lost
    "AZ": 3,  # lost
    "BZ": 9,  # won
    "CZ": 6,  # draw
}
scores = [scoring_map[round] for round in rounds]
print(sum(scores))

winner_map = {
    "A": "Y",
    "B": "Z",
    "C": "X",
}
loser_map = {
    "A": "Z",
    "B": "X",
    "C": "Y",
}
draw_map = {
    "A": "X",
    "B": "Y",
    "C": "Z",
}


def convert_end_state_to_move(round: str) -> str:
    match round[1]:
        case "X":
            round = round[0] + loser_map[round[0]]
        case "Y":
            round = round[0] + draw_map[round[0]]
        case "Z":
            round = round[0] + winner_map[round[0]]
    return round


rounds = [convert_end_state_to_move(round) for round in rounds]
scores = [scoring_map[round] for round in rounds]
print(sum(scores))
