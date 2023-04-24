import task1
import utils

def test_evaluateRound():
    # 1 for Rock, 2 for Paper, and 3 for Scissors
    # 0 if you lost, 3 if the round was a draw, and 6 if you won
    # A for Rock, B for Paper, and C for Scissors
    # X for Rock, Y for Paper, and Z for Scissors
    assert task1.evaluateRound("A X") == (3+1)
    assert task1.evaluateRound("C Z") == (3+3)
    assert task1.evaluateRound("B Y") == (3+2)
    assert task1.evaluateRound("A Y") == (6+2)
    assert task1.evaluateRound("B X") == (0+1)
    assert task1.evaluateRound("A Z") == (0+3)

def test_evaluateStrategy():
    test_strat = utils.readInStrategy("test_strat1.txt")
    assert task1.evaluateStrategy(test_strat) == 15