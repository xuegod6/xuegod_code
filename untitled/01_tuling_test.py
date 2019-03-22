# -*- coding: utf-8 -*-
# @Time    : 2019/3/22 10:36
# @Author  : for 
# @File    : 01_tuling_test.py
# @Software: PyCharm
from urllib import request
import json
def computer(info):
    key='2fc58f256e8c4e1bba723fe2c976b614'
    api='http://www.tuling123.com/openapi/api?key='+key+'&info='+info
    response=request.urlopen(api).read()
    client_json=json.loads(response)
    return 'computer:'+client_json['text']
if __name__ == '__main__':
    a = computer('hello')
    print(a)