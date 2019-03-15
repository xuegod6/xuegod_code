# -*- coding: utf-8 -*-
# @Time    : 2019/3/7 11:06
# @Author  : for 
# @File    : test.py
# @Software: PyCharm
import requests,time
from fake_useragent import UserAgent
from lxml import etree
import re
url = 'https://mp.weixin.qq.com/s?__biz=MzAwMzcyNjA1OA==&mid=2247486021&idx=1&sn=5936b3c5ea91aa25707d9015bc496878&chksm=9b3785c0ac400cd6496c6f48a0aa2ff604153dd03d888da2eb42c0e7313dc3840b80ed198b6f&mpshare=1&scene=1&srcid=&pass_ticket=ZH5MZW31ifEnuJoyUdw4%2BlLYrAKGC%2FxsTpeQasVhvVKyZI4HiLcKnHCWQbWtlttC#rd'

headers = {
    'User-Agent':UserAgent().random
}
response = requests.get(url,headers=headers)

xpath_content = etree.HTML(response.content)

content = xpath_content.xpath('//*[@id="js_content"]/section/section/section/section/section/p/span/text()')
num = 1
with open('新闻.txt','w',encoding='utf-8') as f:
    for i in content:
        try:
            data = re.findall(r'[经济|AI|阿里巴巴|阿里|腾讯|未来|IBM]',i)
            if data:
                data = re.sub(r'\d+',str(num),i)
                f.write(data)
                f.write('\n')
                num += 1
                if num > 8:
                    break
        except Exception as e:
            print(e)