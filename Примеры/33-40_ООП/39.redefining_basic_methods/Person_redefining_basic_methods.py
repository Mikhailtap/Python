class Person:
    '''базовый класс'''
    def __init__(self, name):
        self.name=name
    def speak(self, msg='(Calling the base class)'):
        print(self.name, msg)