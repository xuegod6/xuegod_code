# -*- coding: utf-8 -*-
# @Time : 2018/12/18 10:14 
# @Author : for 
# @File : 03-pyechars-test.py 
# @Software: PyCharm
import re

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
from pyecharts import Map
import numpy as np
attr=gdp_data['地区'].values.tolist()  #省份名
attr=[re.sub('[自治区市省回族维吾尔壮族]', '', i) for i in attr]
v1 = gdp_data['2017年'].values #2016年各省GDP
v2 = pop_data['2017年'].values #2016年各省人口
value=np.round(v1/v2,decimals=2).tolist()   #2016年各省人均GDP，保留两位小数
print(value)
map = Map("2017年全国各省人均GDP地图",title_color="#404a59", title_pos="auto",
    width=1200, height=600)
map.add("人均/万元",attr,value,visual_range=[0,12],maptype="china",is_visualmap=True,
    visual_text_color="#000"
)
map.render("全国各省人均GDP地图.html")











# from pyecharts import Line
# province='河南省'
# attr=gdp_data.columns.tolist()[-1:0:-1]  #年份
#
# v1=gdp_data[gdp_data['地区']==province].values.tolist()[0][-1:0:-1]  #历年GDP数据
# v2=pop_data[pop_data['地区']==province].values.tolist()[0][-1:0:-1]  #历年人口数据
# line = Line(province+"历年GDP与人口变化曲线",title_color="#404a59", title_pos="auto",
#     width=1200, height=600)
# line.add("GDP/亿元", attr, v1, is_stack=True, is_label_show=True)
# line.add("人口/万", attr, v2, is_stack=True, is_label_show=True)
# line.render(province+"历年GDP与人口变化曲线.html")








from pyecharts import Bar

# bar = Bar('2017年各省的GDP人口条形图',title_color='blue',
#           width=1200,height= 600,background_color='white'
#           )
#
# bar.add('GDP/亿元',attr,v1,mark_line=["min","average", "max"])
#
# bar.add('人口/万',attr,v2,is_label_show=True,is_datazoom_show=True,
#         xaxis_label_textsize=10,xaxis_rotate=30,
# mark_line=["min","average", "max"]
#         )
# bar.render('2017年人口.html')
_attr=gdp_data['地区'].values.tolist()  #省份名
attr=[re.sub('[自治区市省回族维吾尔壮族]', '', i) for i in _attr]
value=[]
for i in _attr:
    gdp=gdp_data[gdp_data['地区']==i].values.tolist()[0][-1:0:-1]  #历年GDP数据
    rate=round(gdp[-1]/gdp[0],2)
    value.append(rate)
map = Map("近20年全国各省GDP增长率地图",title_color="#404a59", title_pos="auto",
          width=1200, height=600)
map.add("增长率/倍",attr,value,visual_range=[0, 16],maptype="china",is_visualmap=True,
    visual_text_color="#000"
)
map.render("近20年全国各省GDP增长率地图.html")
