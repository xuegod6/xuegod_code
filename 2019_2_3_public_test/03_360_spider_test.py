# -*- coding: utf-8 -*-
# @Time : 2019/1/3 17:15 
# @Author : for 
# @File : 03_360_spider_test.py 
# @Software: PyCharm

import  requests,time
from urllib import request

url = 'http://image.so.com/zj?ch=beauty&sn=30&listtype=new&temp=1'

headers= {
    'Referer': 'http://image.so.com/z?ch=beauty',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36'
}
str_data = '''ch: beauty
sn: 120
listtype: new
temp: 1
'''
send_data = {}
for data in str_data.splitlines():
    key,value = data.split(': ')

    if key and value:
        send_data[key] = value
# print(send_data)

response = requests.get(url,headers=headers,params=send_data)

json_data = response.json()['list']

for index,src in enumerate(json_data):
    image_url = src['qhimg_url']
    try:
        image_name = './image/'+image_url[-8:]
        request.urlretrieve(url=image_url,filename=image_name)

    except Exception as e:
        print(e)
    else:
        print('{} is download'.format(image_name))
        # time.sleep(1)

