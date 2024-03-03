# classes are user defined bluprint or prototype
# self keyword is mandatory fo calling variable names into method

class Calculator:
    sum = 0 # classes variable
    dif = 0

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        sum = self.a + self.b
        return sum

    def sub(self):
        dif = self.a - self.b
        return dif


obj = Calculator(5,4)
