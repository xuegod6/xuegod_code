# -*- coding: utf-8 -*-
# @Time : 2019/1/10 16:28 
# @Author : for 
# @File : 01_360_spider_test.py 
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
    line_data = data.split(': ')
    if len(line_data) == 2:
                key,value = line_data
                if key and value:
                    send_data[key] = value
response = requests.get(url,headers=headers,params=send_data)
json_data = response.json()['list']
for src in json_data:
    image_url = src['qhimg_url']
    try:
        image_name = './360_image/'+image_url[-8:]
        request.urlretrieve(url=image_url,filename=image_name)
    except Exception as e:
        print(e)
    else:
        print('{} is download'.format(image_name))
