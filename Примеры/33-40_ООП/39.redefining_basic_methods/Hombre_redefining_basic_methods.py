from Person_redefining_basic_methods import*
'''производный класс'''
class Hombre(Person):
    def speak(self, msg):
        print(self.name, ":\n\tHola!", msg)