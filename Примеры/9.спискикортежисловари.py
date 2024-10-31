#12.for__in__.py
chars = ['a', 'b', 'c'] 
'''список - он так оформляется
можно использовать список как матрицу: chars=[[],[]]
поэтому можно добавлять инструкции для отображения значений:
print('\n', chars[0][1]) - для примера 
(#2.work_with_lists.py)'''
fruit = ('apple', 'banana', 'cherry') 
'''кортеж - неизменяемый (фиксированный спиок)
список. Все его значения неизменны на протяжении работы всей программы
создается путем (ВСЕГДА) через запятую и в скобках - упаковка кортежа
к отдельному элементу можно обращаться (set[i], где i - индекс элемента)
все значения внутри кортежа могут быть присвоены отдельным переменным - 
распаковка последовательности (a, b, c = fruit)'''
dict = {'name':'mark', 'sp':'ing'} #словарь - список, где нет повторяющихся элементов
#(#3.work_with_sets.py)
print ('\nElements:\t', end=' ')
for item in chars:
    print (item, end = ' ')
print ('\nEnumerated:\t', end = ' ')
for item in enumerate (chars):
    print (item, end = ' ')
print ('\nZipped:\t', end = ' ')
for item in zip (chars, fruit):
    print (item, end = ' ')
print ('\nPaired:')
for key, value in dict.items():
    print (key, '=', value)