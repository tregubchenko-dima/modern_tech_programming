class Alcohol:

    def __init__(self, name, price, v):
        self.__name = name
        self.__price = price
        self.__v = v

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_v(self):
        return self.__v
