# -*- coding: utf-8 -*-
# @Time    : 2019/2/28 20:55
# @Author  : for 
# @File    : 02_file_test.py
# @Software: PyCharm
import json
data = {"age": 18, 'name': "For", "data": [1, 2, 3]}
with open('data.json','r',encoding='utf-8') as f:
    text = json.load(f)
    print(type(text))