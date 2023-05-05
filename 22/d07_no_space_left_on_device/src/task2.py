from src import task1


def get_smallest_reclaimable_space(console_history):
    SPACE_TOTAL = 70000000
    SPACE_REQUIRED = 30000000
    dtb = DirectoryTreeBuilder(console_history)
    SPACE_ALLOCATED = dtb.root_size
    SPACE_DELTA = SPACE_REQUIRED - (SPACE_TOTAL - SPACE_ALLOCATED)
    index = dtb.dir_size_index
    srs = find_smallest_fitting(index.values(), SPACE_DELTA)
    return srs


def find_smallest_fitting(nums, min_num):
    # binary search
    sorted_nums = sorted(nums)
    MAX = sorted_nums[-1] + 1
    beg = 0
    end = len(nums)-1
    smallest = MAX
    while beg <= end:
        mid = (beg+end)//2
        cand = sorted_nums[mid]
        if cand < min_num:
            beg = mid + 1
        else:
            smallest = min(smallest, cand)
            end = mid-1
    return smallest if smallest < MAX else -1


class DirectoryTreeBuilder(task1.DirectoryTreeBuilder):

    @property
    def root_size(self):
        return self.root.size
