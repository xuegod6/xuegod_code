# -*- coding: utf-8 -*-
# @Time : 2018/12/17 14:48 
# @Author : for 
# @File : 02_reauesgts_test.py 
# @Software: PyCharm

import requests
from urllib import request
import time
url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E5%94%AF%E7%BE%8E&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&hd=&latest=&copyright=&word=%E5%94%AF%E7%BE%8E&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&expermode=&selected_tags=&pn=180&rn=30&gsm=b4&1545029139382='
headers= {
'Referer': 'https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&sf=1&fmq=&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&fm=result&pos=history&word=%E5%94%AF%E7%BE%8E',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36',
}
data_str ='''
tn: resultjson_com
ipn: rj
ct: 201326592
is: 
fp: result
queryWord:唯美
cl: 2
lm: -1
ie: utf-8
oe: utf-8
adpicid: 
st: -1
z: 
ic: 0
hd: 
latest: 
copyright: 
word: 美女
s: 
se: 
tab: 
width: 
height: 
face: 0
istype: 2
qc: 
nc: 1
fr: 
expermode: 
selected_tags: 
pn: 180
rn: 90
gsm: b4
1545029139382: 
'''
send_data = {}
for line in data_str.splitlines():
    line_data = line.split(': ')
    # print(line_data)

    if len(line_data) == 2:
        key,value = line_data

        if key and value:
            send_data[key] = value
# print(send_data)

response  = requests.get(url = url,headers = headers,params=send_data)

content = response.json()['data']

# for i in content:
#     print(i['middleURL'])
for index,src in enumerate(content):
    img_url = src.get('middleURL')
    if img_url:
        name = './image/image_%s_%s.png'%('唯美',index)
        try:
            request.urlretrieve(url = img_url,filename=name)

        except Exception as e:
            print(e)

        else:
            print('%s is down'%name)
        time.sleep(1)








