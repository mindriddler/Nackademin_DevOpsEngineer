
class Calculator:

    def __init__(self) -> None:
        pass

    def addition(self, x, y):
        result = x + y
        return result

    def subtraction(self, x, y):
        result = x - y
        return result

    def division(self, x, y):
        result = x / y
        return result

    def multiplication(self, x, y):
        result = x * y
        return result

    def add_mult(self, x, y):
        result = self.addition(x, y) + self.multiplication(x, y)
        return result

    def clear(self, x):
        x = 0
        return x
