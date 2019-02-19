# -*- coding: utf-8 -*-
# @Time    : 2019/2/18 21:12
# @Author  : for 
# @File    : 03_args_test.py
# @Software: PyCharm
import multiprocessing
def show_info(name,age):
    print(name,age)
    current_process = multiprocessing.current_process()
    print(current_process.name)

if __name__ == '__main__':
    # 创建子进程
    # 1. group:进程组，目前必须使用None，一般不用设置
    # 2. target:执行目标函数
    # 3. name: 进程名称
    # 4. args: 以元组方式给函数传参
    # 5. kwargs: 以字典方式给函数传参
    sub_process = multiprocessing.Process(target=show_info,name='myprocess',kwargs={'name':'for','age':18})
    sub_process.start()