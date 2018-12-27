# -*- coding: utf-8 -*-
# @Time : 2018/12/26 15:47 
# @Author : for 
# @File : models.py 
# @Software: PyCharm
# -*- coding: utf-8 -*-
# @Time : 2018/12/26 15:22
# @Author : for
# @File : __init__.py
# @Software: PyCharm
import peewee

db = peewee.SqliteDatabase('blog.db')

class Article(peewee.Model):

    title = peewee.CharField(max_length=32)
    author = peewee.CharField(max_length=32)
    time = peewee.CharField(max_length=32)
    description = peewee.TextField()
    content = peewee.TextField()
    class Meta:
        database = db

if __name__ == '__main__':
    Article.create_table()
