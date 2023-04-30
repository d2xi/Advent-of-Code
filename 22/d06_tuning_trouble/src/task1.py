from utils import utils

def sop_marker_offset(datastream,frame_len=4):
	beg=0
	end=beg+frame_len
	frame=''
	offset=None
	while end<=len(datastream):
		frame=datastream[beg:end]
		if len(set(frame))==frame_len:
			offset=end
			break
		beg+=1
		end+=1
	return offset