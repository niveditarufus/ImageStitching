import cv2
import numpy as np
import random


def change_light(image, coeff):
    image_HLS = cv2.cvtColor(image, cv2.COLOR_RGB2HLS)
    image_HLS = np.array(image_HLS, dtype = np.float64)
    image_HLS[:, :, 1] = image_HLS[:, :, 1] * coeff
    if coeff > 1:
        image_HLS[:, :, 1][image_HLS[:, :, 1] > 255] = 255
    else:
        image_HLS[:, :, 1][image_HLS[:, :, 1] < 0] = 0
    image_HLS = np.array(image_HLS, dtype = np.uint8)
    image_RGB = cv2.cvtColor(image_HLS, cv2.COLOR_HLS2RGB)
    return image_RGB


def add_blur(image, x, y, hw, fog_coeff):
    overlay = image.copy()
    output = image.copy()
    alpha = 0.08 * fog_coeff
    rad = hw // 2
    point = (x + hw // 2, y + hw // 2)
    cv2.circle(overlay, point, int(rad), (255, 255, 255), -1)
    cv2.addWeighted(overlay, alpha, output, 1 - alpha, 0, output)
    return output


def generate_random_blur_coordinates(imshape, hw):
    blur_points = []
    midx = imshape[1] // 2 - 2 * hw
    midy = imshape[0] // 2 - hw
    index = 1
    while midx > -hw or midy > -hw:
        for i in range(hw // 10 * index):
            x = np.random.randint(midx, imshape[1] - midx - hw)
            y = np.random.randint(midy, imshape[0] - midy - hw)
            blur_points.append((x, y))
        midx -= 3 * hw * imshape[1] // sum(imshape)
        midy -= 3 * hw * imshape[0] // sum(imshape)
        index += 1
    return blur_points


def Augment_Image(img, choice=None):
	if choice is None:
		return img
	else:
		if choice == 'bright':
			img = change_light(img, 1 + np.random.uniform(0,1))
		elif choice == 'dark':
			img = change_light(img, 0.5)
		elif choice=='haze':
			hw = int(img.shape[1] // 3 * 0.9)
			haze_list = generate_random_blur_coordinates(img.shape, hw)
			for haze_points in haze_list:
			    img = add_blur(img, haze_points[0],haze_points[1], hw, 0.9) 
	return img


