# -*- coding: utf-8 -*-
# @Time    : 2019/3/14 20:55
# @Author  : for 
# @File    : 02_image_word_test.py
# @Software: PyCharm
from wordcloud import WordCloud
#todo:z这个是图相处理函数
from scipy.misc import imread
#todo：打开将要生词云的文本
f = open('1.txt','r').read()
#todo:对一张图片进行处理
mk = imread('1.png')

wc = WordCloud(
    mask=mk,
    background_color='white',
    width=500,
    height= 366,
    margin=2
).generate(f)#todo生成队形并且成成一个新的词云
#词云保存在本机
wc.to_file('2.jpg')
