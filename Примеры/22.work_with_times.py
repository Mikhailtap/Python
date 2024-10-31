'''Для работы с системными временем и датой подключаем модуль datetime.
Он содержит объект datatime с атрибутами year, month, day, hour, 
minute, second, microsecond.
Содержит метод today() - присваивает атрибутам объекта значение текущей
даты и времени и возвращает их в виде кортежа.
Содержит метод getattr() - требует два аргумента, указывающих имя объекта
и атрибут, который нужно получить. Альтернативный способ доступа к атрибуту
 - datetime.year. 
 Все значения хранятся в виде числовых величин, могут быть преобразованы 
 в текст с помощью strftime(). Требует передачи единственного строкового
 аргумента (директивы), указывающего, какую часть кортежа и в каком формате
 возвратить. (атрибуты директив today)'''

from datetime import*
today=datetime.today()
print('Today is: ', today)
for attr in \
['year', 'month', 'day', 'hour', 'minute', 'second', 'microsecond']:
    print(attr, ':\t', getattr(today, attr))
print('Time:\t', today.hour, ':', today.minute, sep='')
day=today.strftime('%A')
month=today.strftime('%B')
print('Date:', day, month, today.day) 