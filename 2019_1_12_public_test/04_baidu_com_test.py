# -*- coding: utf-8 -*-
# @Time : 2019/1/12 10:41 
# @Author : for 
# @File : 04_baidu_com_test.py 
# @Software: PyCharm
from bs4 import BeautifulSoup
import requests

url = 'https://tieba.baidu.com/p/5950745302'
#利用reuqests这个模块 进行模拟浏览器访问，得到所有的文本
html = requests.get(url=url).text
# print(html) #把上边得到的文本内容 都变成美丽汤匹配的格式
result = BeautifulSoup(html,'html.parser')
#把上边美丽唐格式的文本 进行搜索我们想要的数据，返回的一个列表
result_imgs = result.find_all('img',class_ = 'BDE_Image')

# print(result_imgs)
#
i = 1
#遍历
for result_img in result_imgs:
    #具体的src中的值 url url 是一个图片文件
    img_url = result_img['src']
    #利用 requests这个模块获取文件图片的所有数据
    result_img_content = requests.get(img_url).content
    #本地起个文件名
    file_name = './images/' + str(i)+'.jpg'
    #打开我们新建的文件，然后写入我们所有刚刚得到的图片文件内容
    with open(file_name,'wb') as f:
        f.write(result_img_content)
    i += 1