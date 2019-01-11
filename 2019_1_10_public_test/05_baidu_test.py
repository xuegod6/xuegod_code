# -*- coding: utf-8 -*-
# @Time : 2019/1/10 20:58 
# @Author : for 
# @File : 05_baidu_test.py 
# @Software: PyCharm
import time,requests
from urllib import request
url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E5%94%AF%E7%BE%8E&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&hd=&latest=&copyright=&word=%E5%94%AF%E7%BE%8E&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&expermode=&force=&pn=120&rn=30&gsm=78&1547125084028='

headers={
'Referer': 'https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=index&fr=&hs=0&xthttps=111111&sf=1&fmq=&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E5%94%AF%E7%BE%8E&oq=%E5%94%AF%E7%BE%8E&rsp=-1',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36'
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
pn: 120
rn: 60
gsm: 78
1547125084028: '''
send_data = {}
for line in data_str.splitlines():
    line_data = line.split(': ')
    # print(line_data)
    if len(line_data) == 2:
        key,value = line_data
        if key and value:
            send_data[key] = value
send_data['queryWord'] = send_data['word'] = '鬼刀'
response = requests.get(url=url,headers = headers,params=send_data)

content  = response.json()['data']

num = 1
for index,src in enumerate(content):
    img_url = src.get('middleURL')
    if img_url:
        name = './baidu_image/image_%s_%s.png'%('唯美',index)
        try:
            request.urlretrieve(url=img_url,filename=name)
            # time.sleep(1)
        except Exception as e:
            print(e)
        else:
            print('%s is down'%name)