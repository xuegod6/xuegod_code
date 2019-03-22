# -*- coding: utf-8 -*-
# @Time : 2018/12/19 17:17 
# @Author : for 
# @File : 08-gongzi_test.py 
# @Software: PyCharm
import pandas as pd
import numpy as np
import re

gdp_path = './static/china_gdp.csv'
pop_path = './static/people_num.csv'

gdp_data = pd.read_csv(gdp_path,encoding='GB2312')
pop_data = pd.read_csv(pop_path,encoding='GB2312')




from pyecharts import Map
import numpy as np
attr = gdp_data['地区'].values.tolist()
attr=[re.sub('[自治区市省回族维吾尔壮族]', '', i) for i in attr]
# print(attr)

v1 = gdp_data['2017年'].values
v2 = pop_data['2017年'].values

value = np.round(v1/v2,decimals=2).tolist()
# print(value)
map = Map('2017各省人居GDP',title_pos='auto',title_color='blue',width=1200,height=600)

map.add('人均万元',attr,value,visual_range=[0,12],maptype='china',is_visualmap=True,visual_text_color='#000')


map.render('./html/全省人居GDP.html')