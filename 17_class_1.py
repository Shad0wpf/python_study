#coding=utf-8

class Demo:
    def hello(self):
        print("Hello World")

if __name__ == "__main__":
    Instance1 = Demo()

    def hello2(self):
        print("Hello2")

    Demo.hello2 = hello2

    Instance1.hello()
    Instance1.hello2()


    @staticmethod
    def hello3():
        print("Hello3")


    Demo.hello3 = hello3
    Demo.hello3()


# 构造函数和析构函数

class Car:
    def __init__(self,n):
        self.num = n
        print("编号为",self.num,"的对象出生了！")

    def __del__(self):
        print("编号为",self.num,"的对象死了!")
    
if __name__ == "__main__":
    Car(111)