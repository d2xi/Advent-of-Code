from src import task1
from utils import utils

def test_isFullyContained_negative():
    assert task1.isFullyContained("2-4,6-8") == False
    assert task1.isFullyContained("2-3,4-5") == False

def test_isFullyContained_positive():
    assert task1.isFullyContained("6-6,4-6") == True
    assert task1.isFullyContained("2-8,3-7") == True

def test_numberFullyContained():
    input = utils.readInput("resources/test_input1.txt")
    assert task1.numberFullyContained(input) == 2
