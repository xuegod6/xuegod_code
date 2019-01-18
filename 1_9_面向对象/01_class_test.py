# -*- coding: utf-8 -*-
# @Time : 2019/1/17 20:23 
# @Author : for 
# @File : 01_class_test.py 
# @Software: PyCharm
school = {
    'Linux':[],
    'Python':[]
}
def register(major,student):
    global school
    if major in school:
        school[major].append(student)
        print('报名成功')
    else:
        print('抱歉啊，我们学校没有你的%s专业'%major)
if __name__ == '__main__':
    student = {
        'name':'for',
        'age':18,
        'gender':'男',
        'major':'Python'
    }
    register(student.get('major'),student)
    print(school)

class Registration:
    def __init__(self):
        self.school={
            'Linux':[],
            'Python':[]
        }
    def register(self,major,student):
        if major in self.school:
            self.school[major].append(student)
            print('报名成功')
        else:
            print('抱歉我们学校没有你要的%s专业'%major)

if __name__ == '__main__':
    student = {
        'name':'for',
        'age':18,
        'gender':'男',
        'major':'Python'
    }
    reg = Registration()
    reg.register(student.get('major'),student)
    print(reg.school)














