# -*- conding:utf-8 -*-
#Author:wzf

class Student():
    name = '类变量'
    age = 0
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print(name)
        print(age)

    def do_homework(self):
        print('homework is ok')

student1 = Student('石头',18)
#student1.do_homework()
#print(student1.name)
#print(Student.name)
class A(object):
    bar = 1

    def func1(self):
        print('foo')

    @classmethod
    def func2(cls):
        print('func2')
        print(cls.bar)
        cls().func1()  # 调用 foo 方法


A.func2()  # 不需要实例化