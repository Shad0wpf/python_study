#conding=utf-8


class Fruit:
    price = 0
    def __init__(self):
        self.__color = "Red"
        self.__city = "昆明"

    def __outputColor(self):
        print(self.__color)

    def __outputCity(self):
        print(self.__city)

    def output(self):
        self.__outputCity()
        self.__outputColor()

    #staticmethod
    def getPrice(self):
        return Fruit.price()

    def setPrice(p):
        Fruit.price = p

if __name__ == '__main__':
    apple = Fruit()
    apple.output()
    print(Fruit.price)

    Fruit.setPrice(30)

    apple.output()
    print(Fruit.price)

