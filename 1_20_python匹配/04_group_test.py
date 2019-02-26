# -*- coding: utf-8 -*-
# @Time    : 2019/2/25 22:35
# @Author  : for 
# @File    : 04_group_test.py
# @Software: PyCharm

# import re
# m = re.match(r'(\w+) (\w+)','For Django while')
# print(m.group(0))

import re
# m = re.match(r"(?P<first_name>\w+) (?P<last_name>\w+)", "Malcolm Reynolds")
# print(m.group('first_name'))
# print(m.group('last_name'))
# print(m.group(2))
# m  =re.match(r'(..)+',"a1b2c3")
# print(m.group(1))

# m = re.match(r"(\d+)\.?(\d+)?", "24")
# print(m.groups('0'))

import re
pattern = re.compile(r'(\w+) (\w+)')
matche = pattern.match('hello world')
print(matche.groups())
print(matche.group())
