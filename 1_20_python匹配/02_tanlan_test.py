# -*- coding: utf-8 -*-
# @Time    : 2019/2/25 22:14
# @Author  : for 
# @File    : 02_tanlan_test.py
# @Software: PyCharm
# import  re
# test_str = '''
# <thead>
#     <tr>
#       <th class = 'ok'>Month</th>
#       <th>Savings</th>
#     </tr>
#   </thead>
# '''
#
# print(re.findall(r'<tr>(.*?)</th>',test_str,re.S))

import re
temp = 'abc123'
# print(re.findall('\\d',temp))
# print(re.findall(r'\d',temp))
print(re.findall(r'^www\..*?m','www.baidu.com'))
print(re.findall(r'^www\..*?m','www.m'))
