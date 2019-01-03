# -*- coding: utf-8 -*-
# @Time : 2019/1/3 11:18 
# @Author : for 
# @File : 03_人脸识别_test.py 
# @Software: PyCharm
import face_recognition

abm_image = face_recognition.load_image_file('abm.png')

unknown_image = face_recognition.load_image_file('jh.jpg')

abm_face_encoding = face_recognition.face_encodings(abm_image)[0]
print('chen_face_encoding:{}'.format(abm_face_encoding))

unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]
print('unknow_face_encoding:{}'.format(unknown_face_encoding))

known_faces = [
    abm_face_encoding

]
result = face_recognition.compare_faces(known_faces,unknown_face_encoding)

print('result is {}'.format(result))
print('这个面孔是奥巴马吗{}'.format(result[0]))
print('这个未知的面孔是我们的新面孔吗{}'.format(not True in result ))
