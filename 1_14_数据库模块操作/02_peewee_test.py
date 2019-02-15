# -*- coding: utf-8 -*-
# @Time    : 2019/2/14 22:00
# @Author  : for 
# @File    : 02_peewee_test.py
# @Software: PyCharm
import peewee
import datetime
connect = peewee.MySQLDatabase(
    database='new_test',
    host = '127.0.0.1',
    user = 'root',
    passwd = '123456'
)
class School(peewee.Model):
    name = peewee.CharField(max_length=20,default='for')
    address = peewee.CharField(max_length=30,default='xuegod')
    age = peewee.IntegerField(default=18)
    birthday = peewee.DateTimeField(default=datetime.datetime.now())
    class Meta:
        database = connect
if __name__ == '__main__':
    # School.create_table()
    # s = School.create(name ='for',age =12,birthday = '2017-10-10')
    # s.save()
    # School.insert(name = '小龙女',age = 18,birthday = '2018-6-12').execute()

    # School.update(name = '杨过',age = 10).where(School.id==1).execute()

    #删除数据
    # s = School.get(name = '杨过')
    # s.delete_instance()
    # School.delete_by_id(2)
    # School.delete().where(School.id == 5).execute()

    #查询
    # s = School.select()
    # for i in s:
    #     print(i.name,i.age)

    # s = School.get(School.id == 2)
    # print(s.name,s.age)

    # s = School.select().where(School.id == 2)
    # for i in s :
    #     print(i.name)

    s = School.select().order_by(School.age.asc())
    s = School.select().order_by(School.age.dasc())
    for i in s:
        print(i.age)