from src import task1
from src import task2
from utils import utils

if __name__ == '__main__':
	input = utils.read_input("resources/input.txt")
	print("Tast 1 :", task1.count_visible_trees(input))
	print("Tast 2 :", task2.get_max_scenic_score(input))