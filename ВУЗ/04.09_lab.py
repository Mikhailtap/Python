import math
print ("Лаба 1 расчет сложной конструкции вариант 1")
print ("Hello, plz enter your var:")
x = float (input("[0.1 : 0.6]   "))
pi=math.pi
a = math.sqrt (math.exp(2.2 * x))
b = (pi * x)/(x + 2/3)
c = math.fabs (math.sin (b))
answer = a - c + 1.7
print (round (answer, 4))