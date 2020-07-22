import cv2
import imutils
from augmentation import Augment_Image

images = []
im1 = cv2.imread('./images/left.jpg')
im2 = cv2.imread('./images/right.jpg')

# to choose an effect 
im1 = Augment_Image(im1, 'haze')
im2 = Augment_Image(im2, 'dark')

images.append(im1)
images.append(im2)
if imutils.is_cv3() :
	stitcher = cv2.createStitcher() 
else:
	stitcher = cv2.Stitcher_create()

(status, stitched) = stitcher.stitch(images)
cv2.imwrite('./output/out.jpg', stitched)