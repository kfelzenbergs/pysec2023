
class Calc(object):

    def sum(self, a, b):
        return a + b

    def divide(self, a, b):
        return a / b


mycalc = Calc()
res = mycalc.sum(1, 2)
print(res)
res = mycalc.divide(2, 3)
print(res)
