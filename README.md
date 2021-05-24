# combine_directories.py

You are given two directories: dir1 and dir2.

each directory contain several files and sub directories inside.

For example:

dir1

dir1/file1

dir1/file2

dir1/sub_dir1

dir1/sub_dir1/fileA

dir1/sub_dir2

dir1/sub_dir2/fileZ
 
dir2

dir2/file1

dir2/file2

dir2/sub_dir1

dir2/sub_dir1/fileA

dir2/sub_dir3

dir2/sub_dir3/fileB
 
You will need combine dir1 and dir2 into a new directory named 'new_dir'

if you see a file in dir1 and a file in dir2 have the same filename, please rename the file from dir2 (for example, 'file1' -> 'file1_2'). 

The same rule will apply to the files inside a sub directory as well.

After the combination, dir1 and dir2 should be removed and new_dir will be the only directory left.
