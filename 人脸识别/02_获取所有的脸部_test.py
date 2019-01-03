# -*- coding: utf-8 -*-
# @Time : 2019/1/3 10:46 
# @Author : for 
# @File : 02_获取所有的脸部_test.py 
# @Software: PyCharm
from PIL import Image

import face_recognition

image = face_recognition.load_image_file('jh.jpg')

face_locations = face_recognition.face_locations(image)

print('I found {} faces in this photograph'.format(len(face_locations)))

for face_location in face_locations:
    top,right,bottom,left = face_location
    print(
        "A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))
    # 指定人脸的位置信息，然后显示人脸图片
    face_image = image[top:bottom, left:right]
    pil_image = Image.fromarray(face_image)
    pil_image.save(str(top)+'.jpg')
