class Shop():
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def buy(self):
        return self.quantity*self.price

pay = Shop("корочка хлеба", 1000, 10)
print("Заплатите ", pay.buy(), "гривен за корчки хлеба")