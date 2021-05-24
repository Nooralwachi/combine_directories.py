import os
import shutil
def combine_directories(folder1, folder2):
	dir_dic = {}
	for root, dirs, files in os.walk(folder1):
		for file in files:
			sub_dir = '/'.join(root.split('/')[1:])
			sub_dir_file = sub_dir + '/' + file
			dir_dic[sub_dir_file] = root + '/' + file
	print(dir_dic)

	for root, dirs, files in os.walk(folder2):
		for file in files:
			sub_dir = '/'.join(root.split('/')[1:])
			sub_dir_file = sub_dir + '/' + file
			full_dir_file = root + '/' + file
			if sub_dir_file in dir_dic:
				os.rename(full_dir_file,  dir_dic[sub_dir_file] + '_2')
			else:
				os.makedirs(folder1 + '/' + sub_dir, exist_ok=True)
				os.rename(full_dir_file, folder1 + '/' + sub_dir_file)
	os.rename(folder1, 'new_dir')
	shutil.rmtree(folder2, ignore_errors=True)
	return

combine_directories('dir1', 'dir2')