from utils import utils


def count_visible_trees(input):
    heights = str_to_array2d(input)
    visibility_mask = get_visibility_mask_2d(heights)
    return count_visible(visibility_mask)


def str_to_array2d(input):
    lines = input.strip().splitlines()
    list_2d = [list(map(int, line)) for line in lines]
    return list_2d


def count_visible(list_2d):
    return sum(map(sum, list_2d))


def get_visibility_mask_2d(list_2d):
    mask_cols = visibilty_mask_cols(list_2d)
    mask_rows = visibilty_mask_rows(list_2d)
    return [or_elementwise(*row) for row in zip(mask_cols, mask_rows)]


def visibilty_mask_cols(list_2d):
    num_cols = len(list_2d[0])
    mask_2d = []
    for id in range(num_cols):
        col = get_column(id, list_2d)
        mask_2d.append(get_visibility_mask_1d(col))
    return transpose(mask_2d)


def transpose(list_2d):
    num_cols = len(list_2d[0])
    return [get_column(id, list_2d) for id in range(num_cols)]


def visibilty_mask_rows(list_2d):
    num_rows = len(list_2d)
    mask_2d = []
    for id in range(num_rows):
        row = get_row(id, list_2d)
        mask = get_visibility_mask_1d(row)
        mask_2d.append(mask)
    return mask_2d


def get_column(id, list_2d):
    return [row[id] for row in list_2d]


def get_row(id, list_2d):
    return list_2d[id]


def get_visibility_mask_1d(int_list):
    mask_side_one = find_first_ascending_sequence(int_list)
    mask_side_two = find_first_ascending_sequence(int_list[::-1])
    return or_elementwise(mask_side_one, mask_side_two[::-1])


def or_elementwise(list1, list2):
    return [a | b for (a, b) in zip(list1, list2)]


def find_first_ascending_sequence(int_list):
    in_first_asc_seq = []
    if int_list:
        in_first_asc_seq.append(1)
        last = len(int_list) - 1
        beg = 0
        end = beg + 1
        while end <= last:
            val_beg = int_list[beg]
            val_end = int_list[end]
            if val_beg < val_end:
                in_first_asc_seq.append(1)
                beg = end
            else:
                in_first_asc_seq.append(0)
            end += 1
    return in_first_asc_seq
