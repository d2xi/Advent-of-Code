from utils import utils
from src import task1

def test_sop_marker_offset():
    assert task1.sop_marker_offset("bvwbjplbgvbhsrlpgdmjqwftvncz")==5
    assert task1.sop_marker_offset("nppdvjthqldpwncqszvftbrmjlhg")==6
    assert task1.sop_marker_offset("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg")==10
    assert task1.sop_marker_offset("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw")==11
    assert task1.sop_marker_offset("mjqjpqmgbljsphdztnvjfqwrcgsmlb")==7