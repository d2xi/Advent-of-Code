from src import task1
from src import task2
from utils import utils

if __name__ == '__main__':
	input=utils.readInput("resources/input.txt")
	print("Task 1: ", task1.sop_marker_offset(input))
	print("Task 2: ", task2.som_marker_offset(input))
	
