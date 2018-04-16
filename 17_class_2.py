#coding=utf-8

import math

# 运算符重载方法

class Vector2(object): 
    '''
    类内完成所有向量的运算，分量为x、y
    需要把对象当做位置，调用getpos()返回元组
    '''

    def __init__(self,x=0.0,y=0.0):
        (self.x,self.y) = (x,y)

    def __getitem__(self,item):
        if item == 0:
            return self.x
        if item == 1:
            return self.y
        
    def __str__(self):
        return "(%s,%s"%(self.x,self.y)

    def get_len(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def normalize(self):
        it = self.get_len()
        self.x /= it
        self.y /= it
    
    def __add__(self,other):
        third = Vector2()
        third.x = self.x + other.x
        third.y = self.y + other.y
        return third
    
    def __sub__(self,other):
        third = Vector2()
        third.x = self.x - other.x
        third.y = self.y - other.y
        return third

    def __mul__(self,other):
        return Vector2(other*self.x,other*self.y)

    def __div__(self,other):
        if other != 0:
            return Vector2(self.x/other,self.y/other)
        else:
            return Vector2(self.x,self.y)

    def getpos(self):
        return(self.x,self.y)

if __name__ == "__main__":
    v1 = Vector2(1,2)
    v2 = Vector2(3,4)

    v3 = (v1 + v2)/2

    v4 = v2 - v1

    print(v1)
    print(v2)
    print(v3)
    print(v4)

    print(str(v4.get_len()))
    print(v3.getpos())