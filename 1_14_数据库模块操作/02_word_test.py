# -*- coding: utf-8 -*-
# @Time    : 2019/2/14 14:48
# @Author  : for 
# @File    : 02_word_test.py
# @Software: PyCharm
from wordcloud import WordCloud
from scipy.misc import imread
f = open('china_word.txt','r',encoding='utf-8').read()
#解析图片 将图片编程一个数组
mk = imread('1.png')
#生成词云
wc = WordCloud(
    mask = mk,
    background_color='white',
    font_path="C:/Windows/Fonts/STFANGSO.ttf",
    width=500,
    height=366,
    margin=2
).generate(f)
#词云保存本地
wc.to_file('./image/1.jpg')