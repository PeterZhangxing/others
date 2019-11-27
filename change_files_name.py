#!/usr/bin/python3.7

import os

BASE_DIR = "C:\\Users\zx\Desktop\FOUND.000"
file_list = os.listdir(BASE_DIR)

for file in file_list:
    if file.split('.')[1] != "jpeg":
        new_file_name = file.split('.')[0] + ".jpeg"
        print(new_file_name)
        os.rename(os.path.join(BASE_DIR,file),os.path.join(BASE_DIR,new_file_name))