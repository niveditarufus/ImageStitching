import cv2
import imutils
import random
from augmentation import Augment_Image

fourcc = cv2.VideoWriter_fourcc(*'MPEG')
shape = (500,375)
writer = cv2.VideoWriter('./output/output.avi',fourcc, 10, shape)
num_views = 2
vid_list = ["./videos/f1.mp4", "./videos/f2.mp4"]
vs_list = []
t = 0

for i in range(num_views):
	vs_list.append(cv2.VideoCapture(vid_list[i]))
while(True):

	if(t%45==0):
		frames = []
		for i in range(num_views):
			frame = vs_list[i].read()[1]
			if frame is not None:
				if i%2 == 0: # alternatively choose an effect
					choices = ['dark', 'bright', 'haze']
					frame = Augment_Image(frame, random.choice(choices) )
				frame = imutils.resize(frame, width = 500)
				frames.append(frame)
			else:
				break
		if(len(frames)==num_views):
			if imutils.is_cv3() :
				stitcher = cv2.createStitcher() 
			else:
				stitcher = cv2.Stitcher_create()
			(status, stitched) = stitcher.stitch(frames)
			if stitched is not None:
				stitched = cv2.resize(stitched,shape)
				cv2.imshow("Frame", stitched)
				key = cv2.waitKey(1) & 0xFF
				if key == ord("q"):
					break
				writer.write(stitched)
		else:
			break;
	t +=1
writer.release()
cv2.destroyAllWindows()

