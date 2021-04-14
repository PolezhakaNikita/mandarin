class triangle():
    def __init__(self, hiqht, wight):
        self.hiqht = hiqht
        self.wight = wight

    def square(self):
        return self.hiqht*self.wight

triangl = triangle(5, 10)
print(triangl.square())
