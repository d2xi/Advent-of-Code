from utils import utils
from src import task2

def test_get_max_scenic_score():
    inpt = utils.read_input("resources/input_test.txt")
    assert task2.get_max_scenic_score(inpt) == 8

def test_calculate_scenic_scores():
    assert task2.calculate_scenic_scores([[2,4],[1,2]],[[3,9],[2,3]],[[5,25],[3,5]],[[11,121],[5,11]]) == [[330,108900],[30,330]]

def test_view_range_map_2d_d2t_direction():
    assert task2.view_range_map_2d_d2t_direction([[1,2,3,4],[1,2,3,4],[1,2,3,4]]) == [[0,0,0,0],[1,1,1,1],[1,1,1,1]]
    assert task2.view_range_map_2d_d2t_direction([[1,1,1,1],[2,2,2,2],[3,3,3,3]]) == [[0,0,0,0],[1,1,1,1],[2,2,2,2]]

def test_view_range_map_2d_t2d_direction():
    assert task2.view_range_map_2d_t2d_direction([[1,2,3,4],[1,2,3,4],[1,2,3,4]]) == [[1,1,1,1],[1,1,1,1],[0,0,0,0]]

def test_view_range_map_2d_l2r_direction():
    assert task2.view_range_map_2d_l2r_direction([[1,2,3,4],[1,2,3,4],[1,2,3,4]]) == [[1,1,1,0],[1,1,1,0],[1,1,1,0]]
 
def test_view_range_map_2d_r2l_direction():
    assert task2.view_range_map_2d_r2l_direction([[1,2,3,4],[1,2,3,4],[1,2,3,4]]) == [[0,1,2,3],[0,1,2,3],[0,1,2,3]]

def test_view_range_map_1d_l2r_direction():
    assert task2.view_range_map_1d_l2r_direction([1,2,3,4]) == [1,1,1,0]
    assert task2.view_range_map_1d_l2r_direction([4,3,2,1]) == [3,2,1,0]
    assert task2.view_range_map_1d_l2r_direction([5,5,5]) == [1,1,0]
    assert task2.view_range_map_1d_l2r_direction([5,1,5,5]) == [2,1,1,0]
    assert task2.view_range_map_1d_l2r_direction([5,1,5,1,5]) == [2,1,2,1,0]

