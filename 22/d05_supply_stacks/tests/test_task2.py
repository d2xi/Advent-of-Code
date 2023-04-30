from utils import utils
from src import task2

def test_getCratesOnTopAfterRearrangement():
	test_input = utils.readInput("resources/input_test.txt")
	assert task2.getCratesOnTopAfterRearrangement(test_input) == "MCD"
