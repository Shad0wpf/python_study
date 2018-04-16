#coding=utf-8

class Person(object):
    sex = "male"
    def __init__(self,s1,s2):
        self.ID = s1
        self.name = s2
        print("__init__(self) of persion")


    def hello(self,friend):
        print('hello',friend,"!")

class Student(Person):
    def __init__(self,num):
        self.num = num


    def fun(self):
        print(self.ID,self.name,self.num,Student.sex)

class Teacher(Person):
    def __init__(self,s1,s2,t):
        self.title = t
        super(Teacher,self).__init__(s1,s2)
        #也可以通过Persion.__init__(self,s1,s2)

    def fun(self):
        print(self.ID,self.name,self.title,Teacher.sex)

if __name__ == "__main__":
    stu1 = Student("20180101")
    stu1.ID = "000123123"
    stu1.name = "小明"
    stu1.fun()
    stu1.hello("Y")

    te1 = Teacher("123123123","王老师","数学老师")
    te1.fun()