from src import task1
from src import task2
from utils import utils

if __name__ == '__main__':
	input = utils.readInput("resources/input.txt")
	print("Tasks 1: ", task1.getCratesOnTopAfterRearrangement(input))
	print("Tasks 2: ", task2.getCratesOnTopAfterRearrangement(input))
