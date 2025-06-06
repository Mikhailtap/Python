import matplotlib.pyplot as plt # type: ignore
import math
#import sys
#import logging
# объявление и инициализация данных
x=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4]

y= [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
y1=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
y2=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
y3=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
y4=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
y5=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
y6=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
y7=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
y8=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
y9=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
y10=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

f1=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0] 

#интеративное вычисление сложной формулы по частям
for i in range(6):
    y1[i]=2/3
    y10[i]=math.log(x[i])
    if y10[i]<0:
        y10[i]=abs(y10[i])
        y2[i]=(-1)*y10[i]**y1[i]
        pass
    else: y2[i]=y10[i]**y1[i] #вот здесь комплексное число начинается
    y3[i]=math.pi*x[i]
    y4[i]=math.cos(y3[i])
    y5[i]=math.tan(y4[i])
    y6[i]=x[i]/10.5
    y7[i]=math.log(y6[i])
    y8[i]=math.fabs(y7[i])
    y9[i]=y2[i]+y5[i]
    y[i]=y9[i]*y8[i]
    #доп печать с округлением значения функции до 3 знаков после зпт
    print(x[i], round(y[i], 3))
    #logging.basicConfig(level=logging.DEBUG, filename="thecode.log")
    #sys.stderr=open("stderr.txt", "a")
    f1[i]=x[i]
#рисуем график 
plt.plot([x], [y], 'o-.', labe='сложная функция')
plt.plot([x], [f1], 'o--', labe='линейная функция y=x')  
plt.legend(loc= 'upper right')
plt.grid(True)
plt.xlabel('аргумент x=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3,1.4]')
plt.xlim([0.1,1.4])

plt.ylabel('y функция от х')
plt.ylim([0, 1.4])
plt.title('сравнение функций')
plt.show()