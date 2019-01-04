# -*- coding: utf-8 -*-
# @Time : 2019/1/4 20:59 
# @Author : for 
# @File : 01_闰年_test.py 
# @Software: PyCharm
#输入一个数据列幸的字符串 有int强制转换数字
year = int(input('请输入一个年份:'))
#判断！ 判断是不是能够被4整除！ 别00不整除 被400整除
if (year % 4) == 0 and (year % 100) != 0 or (year % 400) == 0:

    print('{0}是闰年'.format(year))
else:
    print('{0}不是闰年'.format(year))
