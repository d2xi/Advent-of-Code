from src.task1 import numberFullyContained
from src.task2 import numberOverlappingPairs
from utils import utils

if __name__ == "__main__":
    input = utils.readInput("resources/input1.txt")
    print("Task1: ", numberFullyContained(input))
    print("Task2: ", numberOverlappingPairs(input))