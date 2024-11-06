from Duck_realizing_polymorphizm import*
from Mouse_realizing_polymorphizm import*
def describe(object):
    object.talk()
    object.coat()
donald=Duck()
mickey=Mouse()
describe(donald)
describe(mickey)