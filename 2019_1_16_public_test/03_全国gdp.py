# -*- coding: utf-8 -*-
# @Time : 2019/1/16 13:38 
# @Author : for 
# @File : 03_全国gdp.py 
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
v1=gdp_data['2017年'].values #2016年各省GDP
v2=pop_data['2017年'].values #2016年各省人口
value=np.round(v1/v2,decimals=2).tolist()   #2016年各省人均GDP，保留两位小数
print(value)
map = Map("2017年全国各省人均GDP地图",title_color="#404a59", title_pos="auto",
    width=1200, height=600)
map.add("人均/万元",attr,value,visual_range=[0,12],maptype="china",is_visualmap=True,
    visual_text_color="#000"
)
map.render("全国各省人均GDP地图.html")
