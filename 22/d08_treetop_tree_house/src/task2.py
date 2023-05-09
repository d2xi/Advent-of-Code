from utils import utils
from src.task1 import str_to_array2d

def get_max_scenic_score(input):
	tree_heights = str_to_array2d(input)
	sce_sco_1 = view_range_map_2d_t2d_direction(tree_heights)
	sce_sco_2 = view_range_map_2d_d2t_direction(tree_heights)
	sce_sco_3 = view_range_map_2d_l2r_direction(tree_heights)
	sce_sco_4 = view_range_map_2d_r2l_direction(tree_heights)
	scenic_scores = calculate_scenic_scores(
		sce_sco_1, sce_sco_2, sce_sco_3, sce_sco_4)
	return max([max(subscores) for subscores in scenic_scores])


def calculate_scenic_scores(list1, list2, list3, list4):
    def mult4(a, b, c, d): return a*b*c*d

    scenic_scores = [[mult4(*entry) for entry in zip(*row)]
                     for row in zip(list1, list2, list3, list4)]

    return scenic_scores


def view_range_map_2d_d2t_direction(list_2d):

    view_ranges_2d = []
    for list_1d in zip(*list_2d):  # tuple = column
        view_ranges_2d.append(
            view_range_map_1d_l2r_direction(list_1d[::-1])[::-1])

    return [list(tup) for tup in zip(*view_ranges_2d)]


def view_range_map_2d_t2d_direction(list_2d):

    view_ranges_2d = []
    for list_1d in zip(*list_2d):  # tuple = column
        view_ranges_2d.append(view_range_map_1d_l2r_direction(list_1d))

    return [list(tup) for tup in zip(*view_ranges_2d)]


def view_range_map_2d_l2r_direction(list_2d):
    view_ranges_2d = []
    for list_1d in list_2d:
        view_ranges_2d.append(view_range_map_1d_l2r_direction(list_1d))

    return view_ranges_2d


def view_range_map_2d_r2l_direction(list_2d):
    view_ranges_2d = []
    for list_1d in list_2d:
        view_ranges_2d.append(
            view_range_map_1d_l2r_direction(list_1d[::-1])[::-1])

    return view_ranges_2d


def view_range_map_1d_l2r_direction(list_1d):
    num_trees = len(list_1d)
    last = num_trees-1
    view_range_counts = []
    for beg in range(num_trees):
        val_beg = list_1d[beg]
        end = beg+1  
        view_range = 0
        while end <= last:
            val_end = list_1d[end]
            view_range += 1
            if val_beg <= val_end:
                break
            end += 1
        view_range_counts.append(view_range)

    return view_range_counts
