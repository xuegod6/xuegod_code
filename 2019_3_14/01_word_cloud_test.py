# -*- coding: utf-8 -*-
# @Time    : 2019/3/14 20:42
# @Author  : for 
# @File    : 01_word_cloud_test.py
# @Software: PyCharm
from wordcloud import WordCloud

f = open('2.txt','r',encoding='utf-8').read()

wc = WordCloud(
    background_color='white',
    width = 500,
    font_path="C:/Windows/Fonts/STFANGSO.ttf",
    height=366,
    margin= 2
).generate(f)

wc.to_file('2.jpg')