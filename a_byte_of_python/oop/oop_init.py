class Person:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print('Hello', self.name, ', how are you?')


p = Person('steven')
p.say_hi()
