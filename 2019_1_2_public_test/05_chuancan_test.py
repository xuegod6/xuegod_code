# -*- coding: utf-8 -*-
# @Time : 2019/1/2 15:31 
# @Author : for 
# @File : 05_chuancan_test.py 
# @Software: PyCharm
def outer(info):
    def Dec(func):

        def inner(name):
            print('info is %s'%info)
            func(name)
            print('come from china')
        return inner
    return Dec
@outer('for is cool')
#func1 = outer('for is cool')(func1)
def func1(name):
    print('this is xueogd1')
    print('I am %s'%name)
#精讲视频  源码 图片 课件
if __name__ == '__main__':
    func1('for')