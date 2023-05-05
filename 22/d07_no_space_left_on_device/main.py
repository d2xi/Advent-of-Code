from src import task1
from src import task2
from utils import utils

if __name__ == '__main__':
    console_history = utils.read_input("resources/input.txt")
    print("Task 1: ", task1.get_reclaimable_space(console_history))
    print("Task 2: ", task2.get_smallest_reclaimable_space(console_history))
