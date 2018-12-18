# -*- coding: utf-8 -*-
# @Time : 2018/12/15 10:38 
# @Author : for 
# @File : 23-shizan-test.py 
# @Software: PyCharm
from urllib import request
from lxml import etree

req = request.Request('https://www.woyaogexing.com/tupian/weimei/')
content = request.urlopen(req).read()
# print(content)
xpath_contnet = etree.HTML(content)

img_list = xpath_contnet.xpath('//*[@id="main"]/div/div/div/div/a/img/@src')

# print(img_list)
# http://img2.woyaogexing.com/2018/12/15/b739d0a3fd6749929918ed9c5640b517!380x240.jpeg
for i in range(len(img_list)):

    img_test = 'http:'+img_list[i]
    req = request.urlopen(img_test).read()

    filename = './image/'+str(i)+'.png'

    with open(filename,'wb') as f:
        f.write(req)


from PIL import Image
import os
width_i = 380
height_i = 240

line_max = 3
row_max = 3
all_path = []

for root,dirs,files in os.walk('./image/'):
    for file in files:
        if 'png' in file:
            all_path.append(os.path.join(root,file))
# print(all_path)

pic_amx = line_max * row_max

num = 0
toImage  = Image.new('RGBA',(width_i * line_max,height_i*row_max))

for j in range(0,line_max):

    for i in range(0,row_max):

        pic_file_head = Image.open(all_path[num])

        tmmpic = pic_file_head.resize((width_i,height_i))

        loc = (int(i % line_max *width_i),int(j % line_max*height_i))

        toImage.paste(tmmpic,loc)

        num  = num + 1

        if num > pic_amx:
            break
toImage.save('./static/peijine.png')

