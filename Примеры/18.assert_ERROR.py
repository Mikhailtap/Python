''' assert - инструкция, проверяющая текстовое выражение на True-False.
если проверка не пройдена, то ошибка AssertionError. Проверка пройдена - 
функция не делает ничего.
!!!РАЗНИЦА!!! между исключениями и assert - исключения предлагают способ
для обработки ошибок, а assert - средство для нахождения ошибок во время 
работы над программой.'''

chars = ['A', 'B', 'G', 'D', 'E']
def display (elem):
    assert type(elem) is int, 'Arguement must be integer!'
    #сверху - проверочное выражение, описательное сообщение
    print ('List element', elem, '=', chars[elem])
elem = 4
display (elem)
elem = elem/2
display (elem)