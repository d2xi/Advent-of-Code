# points for the outcome
rock        = {"X":{"A":3,"B":0,"C":6}}
paper       = {"Y":{"A":6,"B":3,"C":0}}
scissors    = {"Z":{"A":0,"B":6,"C":3}}

# add point for particular choice
rockPicked = 1
paperPicked = 2
scissorsPicked = 3
rock["X"] = {key: value + rockPicked for key, value in rock["X"].items()}
paper["Y"] = {key: value + paperPicked for key, value in paper["Y"].items()}
scissors["Z"] = {key: value + scissorsPicked for key, value in scissors["Z"].items()}

# total points for each possible round
scores = {}
scores.update(rock)
scores.update(paper)
scores.update(scissors)

def evaluateStrategy(strategy):
    rounds = strategy.strip().split("\n")
    scores = map(evaluateRound,rounds)
    totalScore = sum(scores)
    return totalScore

def evaluateRound(round):
    (they,me)=round.strip().split(" ")
    return scores[me][they]


if __name__ == "__main__":
    import utils
    task = utils.readInStrategy("task1.txt")
    print("Task1: ", evaluateStrategy(task))