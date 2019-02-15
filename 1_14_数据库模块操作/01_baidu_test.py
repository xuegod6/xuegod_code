# -*- coding: utf-8 -*-
# @Time    : 2019/2/15 10:27
# @Author  : for 
# @File    : 01_baidu_test.py
# @Software: PyCharm
import requests
from urllib import request
import time
url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E5%94%AF%E7%BE%8E%E5%9B%BE%E7%89%87&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&hd=&latest=&copyright=&word=%E5%94%AF%E7%BE%8E%E5%9B%BE%E7%89%87&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&expermode=&force=&pn=90&rn=30&gsm=5a&1550197094631='
#模拟浏览器请求头
headers ={
    'Referer': 'https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1550196804331_R&pv=&ic=0&nc=1&z=&hd=&latest=&copyright=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E5%94%AF%E7%BE%8E%E5%9B%BE%E7%89%87&f=3&oq=%E5%94%AF%E7%BE%8E&rsp=0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36'
}
#发送给服务器的数据
data_str = '''
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
pn: 90
rn: 60
gsm: 5a
1550197094631: '''
#对数据进行简单的清洗
send_data ={}
#提取一行数据
for line in data_str.splitlines():
    #对每一行数据进行分割生成list
    line_data = line.split(': ')
    # print(line_data)
    #判断提取有用到数据
    if len(line_data) == 2:
        key,value = line_data
        if key and value:
            send_data[key] = value
# print(send_data)
#请求服务器 利用requests
send_data['queryWord'] = send_data['word'] = '落日'
send_data['rn'] = '30'
response = requests.get(url=url,headers = headers,params= send_data)
# print(response)
#服务器返回的json
content = response.json()['data']
# print(content)
num = 1
#利用枚举方法得到具体的数据内容
for index,src in enumerate(content):
    #提取图片的url地址
    img_url = src.get('middleURL')
    #如果有图片
    if img_url:
        name = './image/image_%s_%s.png'%('唯美',index)
        try:
            #映射到本地，保存图片
            request.urlretrieve(url=img_url,filename=name)
            # time.sleep(1)
        #有报错就生成报错信息
        except Exception as e:
            print(e)
        #没哟报错就韩式图片已经下载
        else:
            print('%s is download'%name)