from src.task1 import getSumOfAllErrorPriorities
from src.task2 import calculatePriorites
from utils import utils

if __name__ == "__main__":    
    input = utils.readInput("resources/input1.txt")
    print("Task1: ", getSumOfAllErrorPriorities(input))
    print("Task2: ", calculatePriorites(input))