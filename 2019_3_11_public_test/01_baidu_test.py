# -*- coding: utf-8 -*-
# @Time    : 2019/3/11 14:57
# @Author  : for 
# @File    : 01_baidu_test.py
# @Software: PyCharm
import requests,time
from urllib import request

url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E5%94%AF%E7%BE%8E&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&hd=&latest=&copyright=&word=%E5%94%AF%E7%BE%8E&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&expermode=&force=&pn=90&rn=30&gsm=5a&1552286898853='

headers ={
    'Referer': 'https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1552286696923_R&pv=&ic=0&nc=1&z=&hd=&latest=&copyright=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E5%94%AF%E7%BE%8E',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36',
}

data_str = '''tn: resultjson_com
ipn: rj
ct: 201326592
is: 
fp: result
queryWord: 美女
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
force: 
pn: 30
rn: 30
gsm: 78
1552286899147: '''
send_data = {}#发送给服务器的
for line in data_str.splitlines():
    line_data = line.split(': ')
    if len(line_data) == 2:
        key,value = line_data
        if key and value:
            send_data[key] = value
send_data['queryWord'] = send_data['word'] = '高圆圆'
response = requests.get(url=url,headers=headers,params=send_data)

content = response.json()['data']#把他变成一个复杂的字典 供我们使用，python

num = 1
for index,src in enumerate(content):
    img_url = src.get('middleURL')
    if img_url:
        name = './image/image_%s_%s.png'%('唯美',index)
        try:
            request.urlretrieve(url=img_url,filename=name)
            # time.sleep(1)
        except Exception as e:
            print(e)
        else:
            print('%s is down'%name)
