# -*- coding: utf-8 -*-
# @Time : 2019/1/9 18:05 
# @Author : for 
# @File : q.py 
# @Software: PyCharm
url = 'http://upos-hz-mirrorks3.acgvideo.com/dspxcode/m190109ws2e8185t3erk002bimbs16gx-1-56.mp4?um_deadline=1547037041&rate=500000&oi=3683615411&um_sign=1e6832d451fcacd171232b97f2609daf&gen=dsp&wsTime=1547037041&platform=html5'
from urllib import request
headers = {
        'User - Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 71.0.3578.80 Safari / 537.36',
    }
response = request.Request(url=url,headers=headers)
res = request.urlopen(response)
print(res)