# -*- coding: utf-8 -*-
# @Time    : 2019/3/7 13:58
# @Author  : for 
# @File    : test.py
# @Software: PyCharm
def outer(num):
    def inner(num_in):
        print('inner ,num_id is %d'%num_in)
        return num + num_in
    return inner
if __name__ == '__main__':
    a = outer(20) # return inner  , a = inner
    print(a(200))