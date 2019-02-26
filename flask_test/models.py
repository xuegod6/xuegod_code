# -*- coding: utf-8 -*-
# @Time : 2019/1/12 19:25 
# @Author : for 
# @File : models.py 
# @Software: PyCharm

import peewee

#指定创建数据库的类型
db = peewee.SqliteDatabase("blog.db")

#用类描述我们的数据表
class Article(peewee.Model):
    """
    1、类名默认为表名
    2、默认有主键id
    """
    title = peewee.CharField(max_length = 32)
    author = peewee.CharField(max_length = 32)
    time = peewee.CharField(max_length = 32)
    description = peewee.TextField()
    content = peewee.TextField()

    class Meta:#元类
        database = db #进行数据库和表的关联

if __name__ == "__main__":
    Article.create_table() #进行数据库同步
