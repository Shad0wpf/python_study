#coding=utf-8

class Car:
    price = 20000    #类属性定义

    def __init__(self,c):
        self.color = c   #实例属性定义

if __name__ == "__main__":
    car1 = Car("Red")
    car2 = Car("Blue")
    print(car1.color,Car.price)

    Car.price = 15000  #修改类属性
    Car.brand = "奥迪"   #添加类属性

    car1.color = "Yellow"    #修改实例属性

    print(car2.color,Car.price,Car.brand)
    print(car1.color,Car.price,Car.brand)