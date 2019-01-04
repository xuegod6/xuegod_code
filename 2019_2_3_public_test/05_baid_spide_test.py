# -*- coding: utf-8 -*-
# @Time : 2019/1/4 11:17 
# @Author : for 
# @File : 05_baid_spide_test.py 
# @Software: PyCharm
import time
import requests
from urllib import request
url = 'http://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E5%94%AF%E7%BE%8E&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=&z=&ic=&hd=&latest=&copyright=&word=%E5%94%AF%E7%BE%8E&s=&se=&tab=&width=&height=&face=&istype=&qc=&nc=1&fr=&expermode=&selected_tags=&pn=30&rn=30&gsm=1e&1545019467831='
headers = {
'Referer': 'http://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word=%E5%94%AF%E7%BE%8E',
"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
}

data_str = '''
tn: resultjson_com
ipn: rj
ct: 201326592
is:
fp: result
queryWord: 唯美
cl: 2
lm: -1
ie: utf-8
oe: utf-8
adpicid:
st:
z:
ic:
hd:
latest:
copyright:
word: 唯美
s:
se:
tab:
width:
height:
face:
istype:
qc:
nc: 1
fr:
expermode:
selected_tags:
pn: 30
rn: 60
gsm: 1e
1545019467831:
'''
send_data = {}
for line in data_str.splitlines():
    line_data = line.split(': ')
    if len(line_data) == 2:
        key,value = line_data
        if key and value:
            send_data[key] = value
response = requests.get(url= url,headers = headers,params=send_data)
content = response.json()['data']
print(content)
num = 1

for index,src in enumerate(content):
    img_url = src.get('middleURL')
    if img_url:
        name = './image/iamge_%s_%s.png'%('唯美',index)
        try:
            request.urlretrieve(url = img_url,filename=name)

        except Exception as e:
            print(e)
        else:
            print('%s is down'%name)
        time.sleep(2)
