# -*- coding: utf-8 -*-
# @Time    : 2019/2/14 22:22
# @Author  : for 
# @File    : 03_sqllite_test.py
# @Software: PyCharm
import peewee
db = peewee.SqliteDatabase('sql.db')

class Teacher(peewee.Model):
    name = peewee.CharField(max_length=20,default='for')
    age = peewee.IntegerField()
    class Meta:
        database = db

if __name__ == '__main__':
    # Teacher.create_table()
    # T = Teacher()
# #     # T.name = 'for'
# #     # T.age = 18
# #     # T.save()
#     T = Teacher().insert(name ='小龙女',age = 18)
#     T.execute()
    T = Teacher.delete().where(Teacher.id == 1)
    T.execute()

    T = Teacher.update(name= 'for').where(Teacher.id ==2)
    T.execute()

    T = Teacher().get(id = 2)
    T = Teacher().get_by_id(2)
    T.name = '杨过'
    T.save()

    T_list = Teacher.select()
    for i in T_list:
        print(i.name,i.age)
    T_list = Teacher.select().order_by(Teacher.age)
    for i in T_list:
        print(i.age,i.name)

    T_list = Teacher.select().where(Teacher.age == 18)
    for i in T_list:
        print(i.name)
    T = Teacher.get(id = 2)
    print(T.name,T.age)
