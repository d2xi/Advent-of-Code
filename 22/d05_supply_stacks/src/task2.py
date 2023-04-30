from src import task1

def getCratesOnTopAfterRearrangement(input):
	return task1.getCratesOnTopAfterRearrangement(input,moveCrates=processMove)

def processMove(move, crateStacks):
    (amount_, from_, to_) = move
    pickedCrates = crateStacks[from_][-amount_:]
    crateStacks[from_][-amount_:] = []
    crateStacks[to_] += pickedCrates
