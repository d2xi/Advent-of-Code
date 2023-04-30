from utils import utils
from src import task2

def test_som_marker_offset():
    assert task2.som_marker_offset("mjqjpqmgbljsphdztnvjfqwrcgsmlb")==19
    assert task2.som_marker_offset("bvwbjplbgvbhsrlpgdmjqwftvncz")==23
    assert task2.som_marker_offset("nppdvjthqldpwncqszvftbrmjlhg")==23
    assert task2.som_marker_offset("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg")==29
    assert task2.som_marker_offset("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw")==26