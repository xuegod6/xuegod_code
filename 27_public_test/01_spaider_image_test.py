# -*- coding: utf-8 -*-
# @Time : 2018/12/27 10:34 
# @Author : for 
# @File : 01_spaider_image_test.py 
# @Software: PyCharm
from urllib import request
import requests,os,time

url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E9%AC%BC%E5%88%80&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=&hd=&latest=&copyright=&word=%E9%AC%BC%E5%88%80&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&expermode=&force=&pn=150&rn=30&gsm=96&1545877953682='

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36',
    'Host': 'image.baidu.com',
    'Referer': 'https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1545877913556_R&pv=&ic=&nc=1&z=&hd=&latest=&copyright=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&hs=2&word=%E9%AC%BC%E5%88%80',
}
data = '''
tn: resultjson_com
ipn: rj
ct: 201326592
is: 
fp: result
queryWord: 鬼刀
cl: 2
lm: -1
ie: utf-8
oe: utf-8
adpicid: 
st: -1
z: 
ic: 
hd: 
latest: 
copyright: 
word: 鬼刀
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
pn: 150
rn: 30
gsm: 96
1545877953682: 
'''
sendData = {}
send_data = data.splitlines()
try:
    for i in send_data:
        data_list = i.split(': ')
        if len(data_list) == 2:
            key,value = data_list
            if key and value:
                sendData[key] = value
except Exception as e:
    print(e)


response = requests.get(url=url,headers=headers,params=sendData)

content = response.json()['data']

for index,src in enumerate(content):
    image_url = src.get('middleURL')
    if os.path.exists('image'):
        pass
    else:
        os.mkdir('image')
    if image_url and os.path.exists('image'):
        name = './image/image_%s.png'%(index)
        try:
            request.urlretrieve(url=image_url,filename=name)
        except Exception as e:
            print(e)
        else:
            print('%s is download'%name)
            time.sleep(1)
# print(content)