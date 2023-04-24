import utils
import task2

def test_makeChoice_draw():
    assert task2.makeChoice("A", "Y") == "A"
    assert task2.makeChoice("B", "Y") == "B"
    assert task2.makeChoice("C", "Y") == "C"

def test_makeChoice_win():
    assert task2.makeChoice("A", "Z") == "B"
    assert task2.makeChoice("B", "Z") == "C"
    assert task2.makeChoice("C", "Z") == "A"

def test_makeChoice_lose():
    assert task2.makeChoice("A", "X") == "C"
    assert task2.makeChoice("B", "X") == "A"
    assert task2.makeChoice("C", "X") == "B"

def test_getRoundPoints():
    assert task2.getRoundPoints("A Y") == 4
    assert task2.getRoundPoints("B X") == 1
    assert task2.getRoundPoints("C Z") == 7

def test_evaluateStrategy():    
    test_strat = utils.readInStrategy("test_strat1.txt")
    assert task2.evaluateStrategy(test_strat) == 12