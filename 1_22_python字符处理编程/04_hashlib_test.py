# -*- coding: utf-8 -*-
# @Time    : 2019/2/28 21:19
# @Author  : for 
# @File    : 04_hashlib_test.py
# @Software: PyCharm
#d26a53750bc40b38b65a520292f69306
#md5
# import hashlib
#
# md5 = hashlib.md5()
#
# md5.update('how to use md5 in '.encode())
# md5.update('python hashlib?'.encode())
#
# print(md5.hexdigest())
#sha1
import hashlib
sha1= hashlib.sha1()
sha1.update('how to use sha1 in '.encode())
sha1.update('python hashlib?'.encode())
print(sha1.hexdigest())
#todo:2c76b57293ce30acef38d98f6046927161b46a44












