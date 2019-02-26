# -*- coding: utf-8 -*-
# @Time : 2019/1/11 20:40 
# @Author : for 
# @File : 02_while_test.py 
# @Software: PyCharm
# n = int(input('请输入一个数字:'))
# result = 1
# i = 1
# while i <= n:
#     result = result * i# 1* 1  2*1  3 * 2 *1
#     i += 1
# print(result)

# def test(n):
#     if n == 1:
#         return 1
#     # n =3
#     #返回3*test(2)  test(2)=返回的是2 * test(1)  test(1) 1
#     #3*2*1
#     return n * test(n - 1)#
#
# while True:
#     n = int(input('清洗呼入你想要的数字'))
#     print(test(n))
def func_test(n):
    return test(n,1)
def test(num,product):
    if num ==1:
        return product
    return test(num-1,num * product)
print(func_test(1000))