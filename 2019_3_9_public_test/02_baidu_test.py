# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 10:32
# @Author  : for 
# @File    : 02_baidu_test.py
# @Software: PyCharm
from bs4 import BeautifulSoup
import requests
#模拟浏览器访问服务器，获取html
html = requests.get('https://tieba.baidu.com/p/5950745302').text
#html转换为bs可以匹配的文本
result = BeautifulSoup(html,'html.parser')
#得到img标签
result_imgs = result.find_all('img',class_ = 'BDE_Image')
#标签遍历
i = 1
for result_img in result_imgs:
    #img标签中的内容src
    img_url = result_img['src']
    #请求内容，获取图片的所有数据
    result_img_contnet = requests.get(img_url).content
    #给本地七个文件名
    file_name = './images/'+str(i)+'.jpg'
    #打开文件名吧数据写入，保存图片
    with open(file_name,'wb')as wf:
        wf.write(result_img_contnet)
    i += 1