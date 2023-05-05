from utils import utils
from src import task1


def test_get_reclaimable_space():
    console_history = utils.read_input("resources/input_test.txt")
    assert task1.get_reclaimable_space(console_history) == 95437
