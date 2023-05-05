from utils import utils
from src import task2


def test_get_reclaimable_space():
    console_history = utils.read_input("resources/input_test.txt")
    assert task2.get_smallest_reclaimable_space(console_history) == 24933642


def test_find_smallest_fitting():
    assert task2.find_smallest_fitting([1, 2, 3, 4, 5], 3) == 3
    assert task2.find_smallest_fitting([1, 3, 5], 4) == 5
    assert task2.find_smallest_fitting([1, 3], 4) == -1
