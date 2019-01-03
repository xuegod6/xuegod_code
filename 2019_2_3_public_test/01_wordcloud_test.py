# -*- coding: utf-8 -*-
# @Time : 2019/1/3 15:06 
# @Author : for 
# @File : 01_wordcloud_test.py 
# @Software: PyCharm
#图片文件处理
from wordcloud import WordCloud
from scipy.misc import imread
#读所有的内容
f = open('zhongwen.txt','r',encoding='utf-8').read()
#解析图片，将图片转换成一个数组
mk = imread('1.png')
#一个实例对象 传递响应的参数
#generate生成词云
wc = WordCloud(
    mask=mk,
    background_color='white',
    width=500,
    height=366,
    font_path="C:/Windows/Fonts/STFANGSO.ttf",
    margin=2
).generate(f)
#把词云一个文件的形式保存搭配本地
wc.to_file('./image/6.png')

