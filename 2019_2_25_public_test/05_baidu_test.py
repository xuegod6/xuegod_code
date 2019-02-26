# -*- coding: utf-8 -*-
# @Time    : 2019/1/25 10:50
# @Author  : for 
# @File    : 05_baidu_test.py
# @Software: PyCharm
import time,requests
from urllib import request

url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E5%94%AF%E7%BE%8E%E5%9B%BE%E7%89%87&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&hd=&latest=&copyright=&word=%E5%94%AF%E7%BE%8E%E5%9B%BE%E7%89%87&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&expermode=&force=&pn=30&rn=30&gsm=1e&1548384663932='

headers = {
    'Referer': 'https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=index&fr=&hs=0&xthttps=111111&sf=1&fmq=&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E5%94%AF%E7%BE%8E%E5%9B%BE%E7%89%87&f=3&oq=wei&rsp=0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36'
}
data_str = '''tn: resultjson_com
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
ic: 0
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
pn: 60
rn: 120
gsm: 1e
1548384663932: 
'''
send_data = {}
#对字符串行分割
for data in data_str.splitlines():
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
# print(send_data)
send_data['word'] = send_data['queryWord'] = '美女'
response = requests.get(url=url,headers=headers,params=send_data)
#吧返回的数据编程python对象
content = response.json()['data']
#进行遍历！
for index,src in enumerate(content):
    #图片的url地址
    img_url = src.get('middleURL')
    if img_url:#如果有
        name = './baidu_image/image_%s_%s.png'%('唯美',index)
        try:
            #下唉到本地
            request.urlretrieve(url=img_url,filename=name)
            # time.sleep(1)
        except Exception as e:
            print(e)
        else:
            print('%s is down'%name)