from Person_redefining_basic_methods import*
'''Производный класс'''
class Man(Person):
    def speak(self, msg):
        print(self.name, ':\n\tHello!', msg)