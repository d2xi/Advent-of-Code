from utils import utils
from src import task1

def som_marker_offset(datastream):
    return task1.sop_marker_offset(datastream,frame_len=14)
