#Безумный ученый Майк развлекается, составляя ряды домино. В качестве 
#домино Майк использует прямоугольные магниты с полюсами «плюс» и «минус». 
#Если друг к другу приблизить два магнита, то одноименные полюса 
#отталкиваются, а разноименные полюса притягиваются.
#Майк начинает с того, что горизонтально кладет на стол один магнит. 
#На каждом следующем шаге Майк продолжает ряд справа, приставляя еще 
#один магнит горизонтально. В зависимости от того, как Майк положил 
#магнит на стол, тот либо притягивается к предыдущему (тогда образуется 
#«островок» из нескольких магнитов вместе), либо отталкивается от 
#предыдущего (тогда Майк кладет новый магнит на некотором расстоянии 
#справа от предыдущего). Считается, что магнит, лежащий отдельно от 
#других, тоже образует свой «островок».
#Майк выложил в ряд несколько магнитов. Определите, сколько «островков» 
#получилось в ряду.
#Входные данные
#Первая строка входных данных содержит целое число n (1 ≤ n ≤ 100000) — 
#количество магнитов. Далее следуют n строк: i-я строка (1 ≤ i ≤ n) 
#содержит символы «01», если Майк положил i-ый по порядку магнит в 
#положении «плюс-минус», и символы «10», если Майк положил этот магнит в 
#положении «минус-плюс».
#Выходные данные
#В единственной строке выходных данных выведите количество «островков», 
#получившихся в ряду.

n = int (input ())
arr = []
count = 0
if 1 <= n <= 100000:
    for i in range (n):
        arr.append (input())
    for i in range (len (arr) - 1):
        a0 = str (arr[i])
        a1 =str (arr[i+1])
        b10 = str (a0[0])
        b11 = str (a0[1])
        b20 = str (a1[0])
        b21 = str (a1[1])
        if b11 == b20:
            count+=1
    print (count + 1)
else:
    print ('No, sorry')