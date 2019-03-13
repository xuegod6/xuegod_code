# -*- coding: utf-8 -*-
# @Time    : 2019/3/13 11:56
# @Author  : for 
# @File    : test.py
# @Software: PyCharm
import os
all_image_path = []
def image_path(dir_name):
    path = os.listdir(dir_name)
    for i in path:
        abs_path = os.path.join(dir_name,i)
        all_image_path.append(abs_path)
image_path(r'E:\xuegod_code\face_django\know_image')
