class Calulator:
    def calculate(self, expression):
        self.value = eval(expression)


class Talker:
    def talk(self):
        print('Hi, my value is', self.value)


class TalkingCalculator(Calulator, Talker):
    pass

tc = TalkingCalculator()

tc.calculate('1 + 2 * 3')
tc.talk()