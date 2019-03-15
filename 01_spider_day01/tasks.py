# -*- coding: utf-8 -*-
# @Time    : 2019/3/5 11:35
# @Author  : for 
# @File    : tasks.py
# @Software: PyCharm
from celery import Celery

app = Celery('tasks',backend='redis',broker='redis://127.0.0.1:6379')

@app.task
def add(x,y):
    return x + y