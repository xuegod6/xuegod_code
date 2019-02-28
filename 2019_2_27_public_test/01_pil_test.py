# -*- coding: utf-8 -*-
# @Time    : 2019/2/28 10:17
# @Author  : for 
# @File    : 01_pil_test.py
# @Software: PyCharm
from urllib import request
from lxml import etree
#访问url
req = request.Request('https://www.woyaogexing.com/tupian/weimei/')
content = request.urlopen(req).read()
#变成xpath对象
xpath_content = etree.HTML(content)
#得到匹配
img_list = xpath_content.xpath('//*[@id="main"]/div/div/div/div/a/img/@src')
for i in range(len(img_list)):
    img_test = 'http:'+img_list[i]
    req = request.urlopen(img_test).read()
    filename = './image/'+str(i)+'.jpg'
    # print(filename)
    with open(filename,'wb') as f:
        f.write(req)
import os
from PIL import Image
import re
# 规定图片大小
width_i=380
height_i=240
# 每行每列的图片数量
line_max=3
row_max=3
# 定义一个空列表
all_path=[]
num=0
# 打开文件 放置图片
for root, dirs, files in os.walk('./image/'):
    for file in files:
        if 'jpg' in file:
            all_path.append(os.path.join(root, file))
# 利用正则 排序
all_path=sorted(all_path, key=lambda i: int(re.search(r'(\d+)', i).group()))
# print(all_path)
# 得到最大的图片数量 9个
pic_max=line_max * row_max
# 生成一个新的画布
toImage=Image.new('RGBA', (width_i * line_max, height_i * row_max))
# 图片处理，这是拼接
for j in range(0, line_max):
    for i in range(0, row_max):
        pic_file_head=Image.open(all_path[num])
        # 重新设置大小
        tmppic=pic_file_head.resize((width_i, height_i))
        # 规定box
        loc=(int(i % line_max * width_i), int(j % line_max * height_i))
        # 黏贴
        toImage.paste(tmppic, loc)
        num=num + 1
        print(num)
        if num > pic_max:
            break
# 报存
toImage.save('Peijie.png')

