# -*- coding: utf-8 -*-
# @Time    : 2019/2/25 20:41
# @Author  : for 
# @File    : 01_re_test.py
# @Software: PyCharm
import re

#匹配自身
# data = re.findall(r'abc','abc')
# print(data)

#\为转义字符,将后面的字符原有语义改变
# data = re.findall(r'www\.baid','www.baidu.c')
# print(data)


#. 任意字符匹配任意字符
# data = re.findall(r'a.c','abc')
# print(data)


#字符集，里面的字符是可以看成b or c or d
#[A-Z]表示单词范围A,B…Z；[a-z]表示小写单词范围a,b…z;[0-9]范围0-9；
# data = re.findall(r'a[0-9]c','a8c')
# print(data)
#\d匹配数字字符
# data = re.findall(r'a\dc','a27c')
# print(data)

# \D 匹配的非数字字符
# data = re.findall(r'a\Dc','ac')
# print(data)
#\s匹配空字符，或者是\n\t\f\v
# data = re.findall(r'a\sc','a\nc')
# print(data)
#\S 匹配非空字符，相当于[^\s]
# data = re.findall(r'a\Sc','a*c')
# print(data)

# \w 匹配单词字符[A-Za-z0-9_]
# data = re.findall(r'a\wc','a_c')
# print(data)

#\W 非单词字符相当于【^\w】
# data = re.findall(r'a\Wc','a c')
# # print(data)

# * 匹配前一个字符0或者是无限次
# data = re.findall(r'abc*','abccccccc')
# print(data)

# + 匹配前一个字符1或者是无限次
# data = re.findall(r'abc+','abcccccc')
# print(data)

#{m}匹配前面的字符m次
# data = re.findall(r'ab{2}','abbc abbc')
# print(data)

#{m,n}匹配前一个字符的m次到n次
# data = re.findall(r'ab{1,2}','abbcabc')
# print(data)
# ^ 匹配字符串开头
# data = re.findall(r'^abc','abcdef')
# print(data)
# # $ 匹配字符串结尾
# data = re.findall(r'ef$','abcdef')
# print(data)

# \A仅匹配字符串开头
# data = re.findall(r'\Aabc','abcdefabc')
# print(data)

# \Z 仅匹配字符串结尾
# data = re.findall(r'abc\Z','abcdefabc')
# print(data)

#\b 单词边界，单词边界就是单词和符号之间的边界
# data = re.findall(r'a\b#bc','a#bc')
# print(data)
# data = re.findall(r'a\Bbc','abc')
# print(data)

# | 代表左右表达式中任意匹配一个[]，它总是先尝试匹配左边的表达式，一旦不成功会跳过匹配右面的表达式
#如果 | 没有被包括在（）中，则它的范围是整个表达式

# data = re.findall(r'abc|def','adcdef')
# print(data)

# data = re.findall(r'(?:abc){2}','abcabc')
# print(data)

# data = re.findall(r'a(123|466)c','a466c')
# # print(data)
# 1.  re.I(re.IGNORECASE): 忽略大小写（括号内是完整写法,下同）；
# 2.  re.M(MULTILINE): 多行模式，改变'^'和'$'的行为；
# 3.  re.S(DOTALL): 点任意匹配模式，改变'.'的行为。
# data = re.findall(r'Hello','hello,world',re.I)
# print(data)
# s = 'i am langzi\nyou are qingren\nshe is xiaosan'
# print(s)
# data = re.findall(r'\W+$',s,re.M)
# print(data)

a = '''asdfhellopass:\n
    123
    worldaf
    '''
b = re.findall('hello(.*)world',a)
c = re.findall('hello(.*)world',a,re.S)

print('b is ',b)
print('c is ',c)
