# -*- coding: utf-8 -*-
# @Time    : 2019/1/25 10:21
# @Author  : for 
# @File    : 04_360_test.py
# @Software: PyCharm
# http://image.so.com/zj?ch=beauty&sn=30&listtype=new&temp=1
# http://image.so.com/zj?ch=beauty&sn=60&listtype=new&temp=1
import requests,time
from urllib import request
url = 'http://image.so.com/zj?ch=beauty&sn=30&listtype=new&temp=1'
headers = {
    'Referer': 'http://image.so.com/z?ch=beauty',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36'
}
str_data = '''ch: beauty
sn: 60
listtype: new
temp: 1
'''
send_data = {}
#对字符串行分割
for data in str_data.splitlines():
    #进行字符串分割 ‘:  返回的是list
    line_data = data.split(': ')
    #判断列表的长度是不是2
    if len(line_data) == 2:
        #系列解包赋值
        key,value = line_data
        #如果 key有值 还有 valur
        if key and value:
            #字典的操作
            send_data[key] = value
response = requests.get(url,headers=headers,params=send_data)
# print(response)
json_data = response.json()['list']
print(json_data)
#枚举方法 会自动给一个索引
for index,src in enumerate(json_data):
    print(index)
    print(src)
    image_url = src['qhimg_url']#获得图片地址
    try:
        #第一步 给比地一个文件的名字
        #第二部 打开文件，把数据保存
        image_name = './360_image/'+image_url[-8:]
        request.urlretrieve(url = image_url,filename=image_name)
    except Exception as e:
        print(e)
    else:
        print('{} is download'.format(image_name))


