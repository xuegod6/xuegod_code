# -*- coding: utf-8 -*-
# @Time    : 2019/2/28 20:38
# @Author  : for 
# @File    : 01_son_test.py
# @Software: PyCharm
# import json
#
# data = {
#     "name":'For',
#     'age':18,
#     "data":[1,2,3]
# }
#
# json_data = json.dumps(data)
# print(json_data)


# loads()

import json
json_data = '{"data": [1, 2, 3], "name": "For", "age": 18}'
data = json.loads(json_data)
print(data['data'])

