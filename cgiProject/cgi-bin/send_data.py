# -*- coding: utf-8 -*-
# @Time : 2018/12/21 9:56 
# @Author : for 
# @File : send_data.py 
# @Software: PyCharm
import json,random,datetime
data = random.randint(1,9)

now = datetime.datetime.now().strftime('%H:%M:%S')

data_dict ={
    'data':data,
    'time':now
}
send_data = json.dumps(data_dict)
#返回数据，也就是发送到前端的数据
#cgi用print作为返回
#返回数据头部
print('Content-type:application/json')
#返回数据结束符
print('\n')
#返回的内容
print(send_data)
# print(type(send_data))