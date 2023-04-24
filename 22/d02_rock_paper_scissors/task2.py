whatDefeats= {
    "A": "B",
    "B": "C",
    "C": "A"
}
whatFailsAgainst= {
    "B": "A",
    "C": "B",
    "A": "C"
}

pointsForOutcome= {
    "X":0, # Lose
    "Y":3, # Draw
    "Z":6, # Win
}

pointsForChoice = {
    "A":1,
    "B":2,
    "C":3,
}

def makeChoice(they, outcome):
    decisions ={
        "X":whatFailsAgainst[they],
        "Y":they,
        "Z":whatDefeats[they]}
    return decisions[outcome]

def getRoundPoints(strat):
    """
        Calculate total number of points for the round.

        - X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win.
        - 0 if you lost, 3 if the round was a draw, and 6 if you won

    Args:
        strat (string): "1 2", where 1 is ["A","B","C"] and 2 is ["X","Y","Z"]

    Returns:
        int: number of points for the strategy 
    """
    (they,outcome)=strat.strip().split(" ")
    totalPointsRound = pointsForOutcome[outcome] + pointsForChoice[makeChoice(they,outcome)]
    return totalPointsRound

def evaluateStrategy(strat):
    rounds = strat.strip().split("\n")
    scores = map(getRoundPoints,rounds)
    totalScore = sum(scores)
    return totalScore

if __name__ == "__main__":
    import utils
    strat = utils.readInStrategy("task1.txt")
    print("Task2: ", evaluateStrategy(strat))
