import sys
sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')

import cv2
import numpy as np

image_name = list()
with open('rgb.txt') as f:
	count = 0
	for line in f.readlines():
		if count >=3:
			image_name.append(line.split()[1])
		count += 1

key_frame_name = []
key_frame_movement = []
count = []
new_count = []

with open('KeyFrameTrajectory.txt') as f:
	for line in f.readlines():
		info = line.split()
		key_frame_name.append('rgb/'+info[0][:-3]+'.png')
		key_frame_movement.append((float(info[1]), float(info[2]), float(info[3]), float(info[4]), float(info[5]), float(info[6]), float(info[7])))

flag = 0
index = 0
i = 0

while i < len(key_frame_name):
	for j in range(len(image_name)):
		if(flag == 0):
			if(key_frame_name[i] == image_name[j]):
				flag = 1
				count.append(0)
				i = i + 1
				break
		elif(flag == 1):
			if(key_frame_name[i] == image_name[j]):
				# if(i >= 2):
				# 	count[index] = count[index] - count[index-1]
				index = index + 1
				flag = 0
				break;
			else:
				count[index] = count[index] + 1

i = 0
while i < len(count):
 	if (i == 0):
 		new_count.append(0)
 		new_count[i] = count[i]
 	else:
 		new_count.append(0)
 		new_count[i] = count[i] - count[i-1]
 	i = i + 1

word_hw6 = cv2.imread('hw6.png')
hw6_keep = word_hw6.copy()

hw6_position_horizontal = 700 # position of center
hw6_position_vertical = 500
keep_position_horizontal = 700 # position of center
keep_position_vertical = 500

flag = False
key_frame_index = 0
is_orz_showed = False
image_array = []
not_key_frame = 0
for img_name in image_name:
	if key_frame_index == len(key_frame_name)-2:
		break
	if img_name == key_frame_name[key_frame_index]:
		not_key_frame = 0
		in_between = new_count[key_frame_index]+1
		key_frame_index += 1
		flag = True
	else:
		not_key_frame += 1

	if not flag:
		continue

	img = cv2.imread(img_name)

	h,w,c = img.shape
	size = (w, h)
	#--- Copy pixel values of logo image to room image wherever the mask is white ---



	scale = ((key_frame_movement[key_frame_index][2]-key_frame_movement[key_frame_index-1][2])/in_between*not_key_frame+key_frame_movement[key_frame_index-1][2])*2.5+1

	width = int(hw6_keep.shape[1]*scale)
	height = int(hw6_keep.shape[0]*scale)
	dim = (width, height)

	if width != word_hw6.shape[1] and height != word_hw6.shape[0]:
		word_hw6 = cv2.resize(hw6_keep, dim, interpolation=cv2.INTER_AREA)

	h_,w_,c_ = word_hw6.shape
	word_hw6_size = (w_, h_)

	ret, hw6_mask = cv2.threshold(word_hw6[:,:,0], 0, 255, cv2.THRESH_BINARY|cv2.THRESH_OTSU)
	hw6_origin = np.where(hw6_mask == 255)

	hw6_position_horizontal = keep_position_horizontal-((key_frame_movement[key_frame_index][0]-key_frame_movement[key_frame_index-1][0])/in_between*not_key_frame+key_frame_movement[key_frame_index-1][0])*1000
	hw6_position_vertical = keep_position_vertical-((key_frame_movement[key_frame_index][1]-key_frame_movement[key_frame_index-1][1])/in_between*not_key_frame+key_frame_movement[key_frame_index-1][1])*1000
	
	for vertical, horizontal in zip(hw6_origin[0], hw6_origin[1]):
		pixel_position = (int(hw6_position_vertical+vertical-h/2), int(hw6_position_horizontal+horizontal-w/2))
		
		if pixel_position[0]>=0 and pixel_position[0]<h and pixel_position[1]>=0 and pixel_position[1]<w:
			img[pixel_position] = word_hw6[(vertical, horizontal)]

	cv2.imshow('result.png', img)
	image_array.append(img)
	cv2.waitKey(30)


video = cv2.VideoWriter('hw6_2.mp4',cv2.VideoWriter_fourcc(*'DIVX'), 15, size)
 
for i in image_array:
    video.write(i)

video.release()

cv2.destroyAllWindows()
