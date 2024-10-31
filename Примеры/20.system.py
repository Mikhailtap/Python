#модуль keyword содержит список всех ключевых слов языка Python, содержащихся
#в его атрибуте kwlist, а также обеспечивает метод iskeyword() для определения
#, является ли слово зарезервированным.
# help -> sys.
import sys, keyword
print ('\nPython version: ', sys.version) #показывает версию системы
print ('\nPython interpreter location: ', sys.executable) #расположение интерпретатора
#в системе
print ('\nPython module search path: ')
for dir in sys.path:
    print (dir)
    #вывод списка всех каталогов, среди котороых интерпретатор производит
    #поиск исполняемых файлов
print ('\nPython keywords: ')
for word in keyword.kwlist:
    print (word)
    #вывод всех ключевых слов Питона