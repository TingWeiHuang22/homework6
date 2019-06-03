import os

dir_path = './8'
rgb_path = dir_path+'/rgb'
for filename in os.listdir(rgb_path):
	print(filename)
	new_name = filename.split('_')[-1]
	print(new_name)
	os.rename(rgb_path+'/'+filename,rgb_path+'/'+new_name)

with open(os.path.join(dir_path,'rgb.txt'),'w') as txt:
	txt.write('# color images\n# file: "rgbd_dataset_freiburg1_xyz.bag"\n# timestamp filename\n')
	for filename in os.listdir(rgb_path):
		if '.png' in filename:
			time = filename.split('.png')[0]
			print(time)
			txt.write(time+' rgb/'+filename+'\n')