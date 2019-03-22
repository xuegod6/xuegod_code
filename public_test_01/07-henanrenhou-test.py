# -*- coding: utf-8 -*-
# @Time : 2018/12/19 16:51 
# @Author : for 
# @File : 07-henanrenhou-test.py 
# @Software: PyCharm
import pandas as pd
import numpy as np

gdp_path = './static/china_gdp.csv'
pop_path = './static/people_num.csv'

gdp_data = pd.read_csv(gdp_path,encoding='GB2312')
pop_data = pd.read_csv(pop_path,encoding='GB2312')

# attr = gdp_data['地区'].values.tolist()
# print(attr)
v1 = gdp_data['2017年'].values.tolist()
v2 = pop_data['2017年'].values.tolist()
from pyecharts import Line
province = '河南省'

attr = gdp_data.columns.tolist()[-1:0:-1]
# print(attr)
v1 = gdp_data[gdp_data['地区']==province].values.tolist()[0][-1:0:-1]

v2 = pop_data[pop_data['地区']==province].values.tolist()[0][-1:0:-1]

line = Line(province+'理念的GDP和人口变化曲线',title_color='blue',title_pos='auto',width=1300,height=600)

line.add('Gdp/亿元',attr,v1,is_stack=True,is_label_show=True)
line.add('人口/万',attr,v2,is_stack=True,is_label_show=True)

line.render('./html/'+province+'理念的GDP和人口变化曲线.html')


