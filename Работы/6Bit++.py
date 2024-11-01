#Классический язык программирования в Битландии — Bit++. 
#Этот язык очень необычный и сложный!
#Особенность языка Bit++ состоит в том, что в нем ровно одна переменная, 
#которая называется x. Также в этом языке есть две операции:
#Операция ++ увеличивает значение, хранящееся в переменной x на 1.
#Операция -- уменьшает значение, хранящееся в переменной x на 1.
#Предложение в языке Bit++ — это последовательность, состоящая из ровно 
#одной операции и ровно одной переменной x. Предложение записывается без 
#пробелов, то есть может содержать только символы: «+», «-», «X». 
#Выполнить предложение, значит выполнить операцию, которая содержится в 
#предложении.
#Программа на языке Bit++ — это последовательность предложений, 
#каждое из которых требуется выполнить. Выполнить программу, значит 
#выполнить все ее предложения.
#Вам задана программа на языке Bit++. Перед выполнением программы в 
#переменной x хранится значение 0. Выполните программу и выведите 
#значение, которое будет храниться в переменной x после выполнения 
#программы.
#Входные данные
#В первой строке записано единственное целое число n (1 ≤ n ≤ 150) — 
#количество предложений в программе. В каждой из следующих n строк 
#записано по предложению. Каждое предложение состоит из ровно одной 
#операции (++ или --) и ровно одной переменной x (обозначается буквой «X»). 
#Таким образом, не бывает пустых предложений. Операция и переменная 
#могут быть записаны в любом порядке.
#Выходные данные
#Выведите единственное целое число — значение, которое будет храниться 
#в переменной x после выполнения программы.

n = int (input())
if 1 <= n <= 50:
    a = 0
    arr = []
    for i in range (n):
        arr.append (input())
        if arr[i] == '++x':
            a+=1
        elif arr[i] == '--x':
            a-=1
        else:
            print ('No no no, its wrong')
    print (a)
else:
    print ('No')