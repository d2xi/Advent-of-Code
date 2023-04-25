from src import task2
from utils import utils

def test_areOverlapping_negative():
    assert task2.areOverlapping("2-4,6-8") == False
    assert task2.areOverlapping("2-3,4-5") == False

def test_areOverlapping_positive():
    assert task2.areOverlapping("6-6,4-6") == True
    assert task2.areOverlapping("2-8,3-7") == True
    assert task2.areOverlapping("2-3,3-7") == True
    assert task2.areOverlapping("4-6,2-4") == True

def test_numberOverlappingPairs():
    input = utils.readInput("resources/test_input1.txt")
    assert task2.numberOverlappingPairs(input) == 4