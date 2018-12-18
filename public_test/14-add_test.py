# -*- coding: utf-8 -*-
# @Time : 2018/12/14 10:26 
# @Author : for 
# @File : 14-add_test.py 
# @Software: PyCharm
import xlsxwriter

workbook = xlsxwriter.Workbook('./static/demo1.xlsx')

wroksheet1 = workbook.add_worksheet()
wroksheet2 = workbook.add_worksheet('foglin1')
wroksheet3 = workbook.add_worksheet('data')
wroksheet4 = workbook.add_worksheet('python')

workbook.close()