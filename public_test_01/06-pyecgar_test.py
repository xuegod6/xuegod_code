# -*- coding: utf-8 -*-
# @Time : 2018/12/19 15:35 
# @Author : for 
# @File : 06-pyecgar_test.py 
# @Software: PyCharm

# from pyecharts import Bar
# v1 =  [1.1, 4.9, 7.0, 23.2, 25.6, 76.7, 120.6, 162.2, 32.6, 20.0, 6.4, 3.3]
# v2 = [5.8, 5.9, 9.0, 26.4, 28.7, 100.7, 195.6, 182.2, 48.7, 18.8, 6.0, 5.7]
# attr = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
#
# bar = Bar('标记线和标记点实力','副标题：展示最大值 最小值 平均值')
#
# bar.add('商家A',attr,v1,mark_line=['min','average','max'])
# bar.add('商家B',attr,v2,mark_line=['min','average','max'])
# # bar.show_config()
# # bar.get_options()
# bar.render('./html/index.html')
# from pyecharts import EffectScatter
# v1 = [10,20,30,40,50,60]
# v2 = [10,20,30,40,50,60]
#
# scatter = EffectScatter('散点图示例')
#
# scatter.add("A",v1,v2)
# # scatter.add("B",v1[::-1],v2)
#
# scatter.render('./html/scatter.html')

#
# from pyecharts import Gauge
#
# gauge = Gauge('仪表盘的示例')
#
# gauge.add('业务指标','完成率',66.66)
#
# gauge.show_config()
# gauge.render('./html/gauge.html')

# from pyecharts import Geo
# data = [('广州',80),('河南',180)]
#
# geo = Geo('全国主要城市空气质量','pm2.5')
#
# attr,value = geo.cast(data)
#
# geo.add('ctiy',attr,value,visual_range=[0,200],maptype='china',visual_text_color='#fff',symbol_size=10,is_visualmap=True)
#
# geo.render('./html/geo.html')

import random
from pyecharts import Map
value = [random.randrange(100) for i in range(5)]

attr = ['许昌市', '郑州市', '开封市', '漯河市', '信阳市市']

map = Map('河南地图示例',width=1200,height=600)

map.add('',attr,value,maptype='河南',is_visualmap=True,visual_text_color='#000')

map.show_config()


map.render('./html/henam.png')







# value = [random.randrange(10,100) for i in range(9)]
#
# attr =["福建", "山东", "北京", "上海", "甘肃", "新疆", "河南", "广西", "西藏"]
#
# map = Map('Map 结合VisualMap示例',width=1200,height=600)
#
# map.add('',attr,value,maptype='china',is_visualmap=True,visual_text_color='#000')
#
# map.render('./html/map.html')








