from src import task1
from utils import utils

def test_findErrorsInRucksack():
    assert task1.findErrorsInRucksack("aa")==["a"]

def test_getPriority():
    assert task1.getPriority("a") == 1
    assert task1.getPriority("z") == 26
    assert task1.getPriority("A") == 27
    assert task1.getPriority("Z") == 52

def test_priorities():
    assert task1.sumPriorities(["A","a"]) == 28
    assert task1.sumPriorities(["B","b"]) == 30

def test_getSumOfAllErrorPriorities():
    input = utils.readInput("resources/input_test1.txt")# do not use ".."
    print(input)
    assert task1.getSumOfAllErrorPriorities(input) == 157