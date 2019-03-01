# -*- coding: utf-8 -*-
# @Time    : 2019/2/28 22:06
# @Author  : for 
# @File    : 07_base64_test.py
# @Software: PyCharm
import base64
data = base64.b64encode('binary\x00string'.encode())
print(data.decode())

de_data = base64.b64decode('YmluYXJ5AHN0cmluZw==')
print(de_data.decode())