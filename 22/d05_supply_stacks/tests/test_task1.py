from utils import utils
from src import task1

def test_parseCrateStacks():
	test_case="[D]         [D]\n[G] [F] [S] [L]\n1   2   3   4"
	assert task1.parseCrateStacks(test_case) == [[],['G','D'],['F'],['S'],['L','D']]

def test_parseMoves():
	test_case="move 1 from 1 to 1\nmove 2 from 2 to 2\nmove 3 from 3 to 3"
	assert task1.parseMoves(test_case) == [(1,1,1),(2,2,2),(3,3,3)]

def test_parseCrateStacks():
	test_case = "[A] [B]    \n[A] [B] [C]\n 1   2   3 "
	assert task1.parseCrateStacks(test_case) == [[], ['A', 'A'], ['B', 'B'], ['C']]


def test_toStackId():
	assert task1.toStackId(3)(0) == 1 
	assert task1.toStackId(3)(12) == 1 
	assert task1.toStackId(4)(12) == 4

def test_intMapper():
	assert task1.intMapper(1) == 0
	assert task1.intMapper(5) == 1
	assert task1.intMapper(9) == 2
	assert task1.intMapper(13) == 3
	assert task1.intMapper(17) == 4

def test_processMove_single_move():
	crateStack = [[], ['A', 'A'], ['B', 'B'], ['C']]
	task1.processMove((2,1,2),crateStack) 
	assert crateStack == [[], [], ['B', 'B', 'A', 'A'], ['C']]

def test_processMove_multiple_moves():
	crateStack = [[], ['A', 'A'], ['B', 'B'], ['C']]
	task1.processMove((2,1,2),crateStack) 
	task1.processMove((4,2,3),crateStack) 
	assert crateStack == [[], [], [], ['C', 'A', 'A', 'B', 'B']]

def test_getCratesOnTopAfterRearrangement():
	test_input = utils.readInput("resources/input_test.txt")
	assert task1.getCratesOnTopAfterRearrangement(test_input) == "CMZ"