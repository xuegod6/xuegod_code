# -*- coding: utf-8 -*-
# @Time : 2018/12/20 14:41 
# @Author : for 
# @File : 09_bar_test.py 
# @Software: PyCharm
# from pyecharts import Bar
# import random
#
# bar = Bar('我的第一个图表','这里是副标题')
#
# bar.add('服装',["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"],[random.randrange(100) for i in range(6)],is_more_utils=True)
#
# bar.show_config()
#
# bar.render()

# import random
#
# v1 = [random.randrange(100)for i in range(12)]
# v2 = [random.randrange(100)for i in range(12)]
# attr = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
# from pyecharts import Bar
# bar = Bar('标题','副标题')
#
# bar.add('商家A',attr,v1,mark_line=['min','average','max'])
# bar.add('商家B',attr,v2,mark_line=['min','average','max'])
#
# bar.render()

# from pyecharts import Geo
#
# data = [('河南',80),('北京',70)]
#
# geo = Geo('全国主要城市空气质量','data from pm 2.5')
# attr,value = geo.cast(data)
# print(attr,value)
# geo.add('city',attr,value,visual_range=[0,100],maptype='china',visual_text_color='#fff',is_visualmap=True)
#
# geo.render()

from pyecharts import Map
value =[155, 10, 66, 78, 33, 80, 190, 53, 49.6]

attr =["福建", "山东", "北京", "上海", "甘肃", "新疆", "河南", "广西", "西藏"]

map = Map('Map',width = 1200,height = 600)

map.add('',attr,value,maptype='china',is_visualmap=True,visual_text_color='#fff')

map.render()








