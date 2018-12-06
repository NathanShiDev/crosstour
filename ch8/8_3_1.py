class MuffedCalcuator:
    muffled = False

    def calc(self, expr):
        try:
            return eval(expr)
        except ZeroDivisionError:
            if self.muffled:
                print('Division by zero is illegal')
            else:
                raise

    def setMuffled(self, value):
        self.muffled = value


calculator = MuffedCalcuator()
calculator.setMuffled(True)
# print('Muffled is True, 1/0', calculator.calc('1/0'))
# print('----------------------------------')
calculator.setMuffled(False)
print('Muffled is False, 1/0', calculator.calc('1/0'))
