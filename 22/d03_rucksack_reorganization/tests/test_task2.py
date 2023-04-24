from utils import utils
from src import task2

def test_splitIntoGroups():
    assert task2.splitIntoGroups("123\n124\n43543\n234\n32423\n32432") == [['123', '124', '43543'], ['234', '32423', '32432']]

def test_identifyGroupBadge():
    assert task2.identifyGroupBadge(["v","v","v"]) == "v"
    assert task2.identifyGroupBadge(["vJrwpWtwJgWrhcsFMMfFFhFp","jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL","PmmdzqPrVvPwwTWBwg"]) == "r"

def test_calculatePriorites():
    inventories = utils.readInput("resources/input_test1.txt")
    assert task2.calculatePriorites(inventories) == 70