#global_a = 1   #!Назначаем глобальную переменную
#к ней можно обратиться изнутри функции
'''def add():
    print (global_a)
    local_a = 2   !Назначаем локальную переменную
    к ней нельзя обратиться изнутри другой функции или извне
    print (local_a)
    global inner_a   !Принудительно назначаем глобальлную переменную
    inner_a = 3
 все, здесь описание функции add() закончилось
add()     Вызываем функцию для выполнения инструкций
print (inner_a)'''

#!!!при конфликте глобальной и локальной переменных будет использоваться
#локальная версия!!!

'''def echo (user, lang, sys):   добавим аргументы (необязательно)
    print (user, lang, sys)
echo ('Mike', 'Python', 'Windows')  вызов  в том же порядке, что и нужно
echo (lang = 'Python', sys = 'Mac OS', user = 'Anne')      произвольный

def mirror (user = 'Carole', lang = 'Python'):   здесь заранее передаем значения
    print ('\n', user, lang)
mirror()
mirror (lang = 'Java')
mirror (user = 'Tony')
mirror ('Susan', 'C++')'''



'''def sum (a, b):
    return a+b
total = sum (8, 4)
print (total)
Возвращаем значение из функции. Разберись получше'''



num = input ('Enter an Integer: ')
def square (num):
    if not num.isdigit():       #Функция проверяет на наличие цифр
        return 'Invalid entry'
    num = int (num)
    return num*num
print (num, '\t', square (num))
#при нахождении не в конце программы, а в ходе ее выполнения, функция
# return при соблюдении условий будет полностью прерывать все последующие
#выполнения инструкций и исполнение программы останавливается. 
# Если не указывать возвращаемое значение, то значение будет None.
# Обычно такое используется если не прошла проверка.
'''def sum(a, b)
    if a<5:
        return
    return a+b     если a<5 то будет возвращаться None''' 