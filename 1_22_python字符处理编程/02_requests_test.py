# -*- coding: utf-8 -*-
# @Time    : 2019/2/28 21:09
# @Author  : for 
# @File    : 02_requests_test.py
# @Software: PyCharm
import requests
import json
url = 'http://image.so.com/zj?ch=beauty&sn=30&listtype=new&temp=1'
req = requests.get(url).json()
print(req['count'])