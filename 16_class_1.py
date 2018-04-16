#coding=utf-8


class Sanjiao:
    def __init__(self,x,y,z):
        self.a = x
        self.b = y
        self.c = z

    def area(self):
        s = (self.a + self.b + self.c)/2
        return (s * (s-self.a)*(s-self.b)*(s-self.c)**(1.0/2))

    def zhouchang(self):
        return self.a + self.b + self.c

if __name__ == "__main__":
    sj1 = Sanjiao(6,6,6)
    sj2 = Sanjiao(3,4,5)

    print("等边三角形的三条边：",sj1.a,sj1.b,sj1.c)
    print("等边三角形的周长：",sj1.zhouchang())
    print("等边三角形的面积：",sj1.area())


    print("直角三角形的三条边：",sj2.a,sj2.b,sj2.c)
    print("直角三角形的周长：",sj2.zhouchang())
    print("直角三角形的面积：",sj2.area())