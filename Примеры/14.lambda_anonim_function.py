#анонимная функция может содержать только одно значение, которое всегда
#должно возвращать значение
#lambda-функция всегда возвращает объект, который разрешается присвоить
#переменной. Впоследствии она может быть использована для того, чтобы 
#обратиться к функции (обратный вызов) в любом месте программы и исполнить
#блок выражений, которые содержит функция
'''def square(x):
    return x**2'''

'''square = lambda x: x**2'''
#называется функцией обратного вызова

x = int(input ('Please enter number: '))

def function_1 (x): return x**2
'''def function_1 (x):
    return x**2'''
def function_2 (x): return x**3
def function_3 (x): return x**4
callback = [function_1, function_2, function_3]  #это список функций 
#Инструкция списков обратных вызовов (сверху)
print ('\nNamed functions: ')
for function in callback: print ('Result:', function (x))
'''for i in callback:
    print('Result:', i(x))'''
#здесь мы сначала перечисляем значения в списке, подставляя в каждую функцию
# - значение наш x, и выводим это на экран.

#для понимания что происходит и как работает:
print('Result of function_1 is:', function_1 (x))

callback = [lambda x: x**2, lambda x: x**3, lambda x: x**4]
'''либо же callback = \
    [lambda x: x**2, lambda x: x**3, lambda x: x**4]
    вот так тоже можно обобщить'''
print ('\nAnonymous functions: ')
for function in callback: print ('result: ', function(x))
#кароче, функция lambda - для краткой обратной функции