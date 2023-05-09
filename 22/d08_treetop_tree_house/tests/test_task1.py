from utils import utils
from src import task1

def test_str_to_array2d():
	assert task1.str_to_array2d('123\n456\n789') == [[1,2,3],[4,5,6],[7,8,9]]
	assert task1.str_to_array2d('1234\n5678\n9123') == [[1,2,3,4],[5,6,7,8],[9,1,2,3]]
        
def test_find_first_ascending_sequence():
      assert task1.find_first_ascending_sequence([])==[]
      assert task1.find_first_ascending_sequence([200])==[1]
      assert task1.find_first_ascending_sequence([5,1])==[1,0]
      assert task1.find_first_ascending_sequence([1,2,3,4,5])==[1,1,1,1,1]
      assert task1.find_first_ascending_sequence([2,1,3,1,4])==[1,0,1,0,1]
      assert task1.find_first_ascending_sequence([5,2,3])==[1,0,0]
      assert task1.find_first_ascending_sequence([5,5,5])==[1,0,0]

def test_get_visibility_mask_1d():
      assert task1.get_visibility_mask_1d([1,2,1]) == [1,1,1]
      assert task1.get_visibility_mask_1d([3,3,3,3,2,1]) == [1,0,0,1,1,1]
      assert task1.get_visibility_mask_1d([1,2,3,3,3,3]) == [1,1,1,0,0,1]
      assert task1.get_visibility_mask_1d([1,2,2,3,3,1,2,1]) == [1,1,0,1,1,0,1,1]

def test_get_column():
      assert task1.get_column(0,[[1,2],[3,4],[5,6]]) == [1,3,5]
      assert task1.get_column(1,[[1,2],[3,4],[5,6]]) == [2,4,6]

def test_get_row():
      assert task1.get_row(0,[[1,2],[3,4],[5,6]]) == [1,2]
      assert task1.get_row(2,[[1,2],[3,4],[5,6]]) == [5,6]

def test_or_elementwise():
      assert task1.or_elementwise([0,0,1,1],[0,1,0,1]) == [0,1,1,1]

def test_visibilty_mask_rows():
      assert task1.visibilty_mask_rows([[1,2,3],[3,1,3],[1,2,3]]) == [[1,1,1],[1,0,1],[1,1,1]]
      assert task1.visibilty_mask_rows([[1,2,3],[3,1,3],[3,1,3],[1,2,3]]) == [[1,1,1],[1,0,1],[1,0,1],[1,1,1]]
      assert task1.visibilty_mask_rows([[1,2,3],[3,1,3],[3,2,1],[1,2,3]]) == [[1,1,1],[1,0,1],[1,1,1],[1,1,1]]
      assert task1.visibilty_mask_rows([[1,2,3],[3,3,3],[3,2,1],[1,2,3]]) == [[1,1,1],[1,0,1],[1,1,1],[1,1,1]]

def test_transpose():
      assert task1.transpose([[1,2,3],[4,5,6],[7,8,9]]) == [[1,4,7],[2,5,8],[3,6,9]]
      assert task1.transpose([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]) == [[1,5,9,13],[2,6,10,14],[3,7,11,15],[4,8,12,16]]

def test_visibilty_mask_cols():
      assert task1.visibilty_mask_cols([[1,2,3],[3,1,3],[1,2,3]]) == [[1,1,1],[1,0,0],[1,1,1]]
      assert task1.visibilty_mask_cols([[1,2,3],[3,1,3],[3,1,3],[1,2,3]]) == [[1,1,1],[1,0,0],[1,0,0],[1,1,1]]
      assert task1.visibilty_mask_cols([[1,2,3],[3,1,3],[3,2,1],[1,2,3]]) == [[1,1,1],[1,0,0],[1,0,0],[1,1,1]]
      assert task1.visibilty_mask_cols([[1,2,3],[3,3,3],[3,2,1],[1,2,3]]) == [[1,1,1],[1,1,0],[1,0,0],[1,1,1]]

def test_get_visibility_mask_2d():
      assert task1.get_visibility_mask_2d([[1,2,3],[3,1,3],[1,2,3]]) == [[1,1,1],[1,0,1],[1,1,1]]
      assert task1.get_visibility_mask_2d([[1,2,3],[3,1,3],[3,1,3],[1,2,3]]) == [[1,1,1],[1,0,1],[1,0,1],[1,1,1]]
      assert task1.get_visibility_mask_2d([[1,2,3],[3,1,3],[3,2,1],[1,2,3]]) == [[1,1,1],[1,0,1],[1,1,1],[1,1,1]]
      assert task1.get_visibility_mask_2d([[1,2,3],[3,3,3],[3,2,1],[1,2,3]]) == [[1,1,1],[1,1,1],[1,1,1],[1,1,1]]

def test_count_visible():
      assert task1.count_visible([[1,1,1],[1,1,1],[1,1,1],[1,1,1]]) == 12
      assert task1.count_visible([[1,1,1],[1,0,1],[1,0,1],[1,1,1]]) == 10

def test_count_visible_trees():
      input = utils.read_input("resources/input_test.txt")
      assert task1.count_visible_trees(input) == 21