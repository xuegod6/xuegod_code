# -*- coding: utf-8 -*-
# @Time    : 2019/2/22 10:48
# @Author  : for 
# @File    : 05_urllib_Test.py
# @Software: PyCharm
from urllib import request

import pyttsx3
from lxml import etree
url ='https://read.qidian.com/chapter/9r9u8W1evJUCpOPIBxLXdQ2/eSlFKP1Chzg1'
#伪造浏览器
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
}
#激进网略请求
req = request.Request(url=url,headers=headers)
response = request.urlopen(req)
content = response.read().decode()
# print(content)#利用xpat获取具体的文本
xpath_content = etree.HTML(content)
new_content = xpath_content.xpath('//*[@id="chapter-382639401"]/div/div/p/text()')

# print(new_content)
with open('3.txt','w',encoding='utf-8') as f:
    for i in new_content:
        f.writelines(i.strip()+'\n')

with open('3.txt','r',encoding='utf-8') as f:
    line = f.read()
    engine = pyttsx3.init()
    engine.say(line)
    engine.runAndWait()




