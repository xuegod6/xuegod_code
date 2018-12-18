# -*- coding: utf-8 -*-
# @Time : 2018/12/11 11:40 
# @Author : for 
# @File : 01-difflib-test.py 
# @Software: PyCharm
import difflib
text1 = '''
This is Text1
人生苦短，我用Python！
Python！Python！Python！
'''
text2 = '''
This is Text2
人生苦短，我用Python！
Python!Python!Python!
'''
text1_lines = text1.splitlines()
text2_lines = text2.splitlines()

# d = difflib.Differ()
# diff = d.compare(text1_lines,text2_lines)
# print('\n'.join(list(diff)))

d = difflib.HtmlDiff()
print(d.make_file(text1_lines,text2_lines))

