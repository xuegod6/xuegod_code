# -*- coding: utf-8 -*-
# @Time : 2019/1/16 13:36 
# @Author : for 
# @File : 02_河南人口.py 
# @Software: PyCharm
import pandas as pd
import numpy
gdp_path = './static/china_gdp.csv'
pop_path = './static/people_num.csv'

gdp_data = pd.read_csv(gdp_path,encoding='GB2312')
pop_data = pd.read_csv(pop_path,encoding='GB2312')

attr = gdp_data['地区'].values.tolist()

# print(attr)

v1 = gdp_data['2017年'].values.tolist()
# print(v1)v
v2 = pop_data['2017年'].values.tolist()
from pyecharts import Line
province='河南省'
attr=gdp_data.columns.tolist()[-1:0:-1]  #年份

v1=gdp_data[gdp_data['地区']==province].values.tolist()[0][-1:0:-1]  #历年GDP数据
v2=pop_data[pop_data['地区']==province].values.tolist()[0][-1:0:-1]  #历年人口数据
line = Line(province+"历年GDP与人口变化曲线",title_color="#404a59", title_pos="auto",
    width=1200, height=600)
line.add("GDP/亿元", attr, v1, is_stack=True, is_label_show=True)
line.add("人口/万", attr, v2, is_stack=True, is_label_show=True)
line.render(province+"历年GDP与人口变化曲线.html")
