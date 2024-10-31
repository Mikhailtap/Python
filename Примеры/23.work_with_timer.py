'''модуль time - позволяет вызывать системное время.
Факт: если вызвать time.time() - возвратит текущее время в секундах, 
прошедшее с 01 января 1970 года (Эра Unix).
Значение, возвращаемое методом time(), может быть преобразовано в объект
struct_time при помощи методов gmtime() и localtime(). Данный объект
содержит атрибуты tm_mon, tm_year, tm_mday, tm_hour, tm_min, tm_sec,
tm_wday, tm_yday и tm_isdst, к которому можно обратиться, используя точеченую
запись. Например, struct.tm_wday.
Все что хранится в struct_time в числовом виде с помощью strftime() может
быть преобразовано в строку. Точно так же, как и в 22. нужна директива.
Есть метод sleep(), который можно использовать для того, чтобы организовывать
паузы в выполнении программы. Аргумент этого метода определяет количество
времени в секундах, на которое необходимо сделать задержку.
Методы localtime() и gmtime() возвращают объект struct_time, имеющий 
атрибуты, в которых содержатся компоненты даты и времени.'''

from time import*
start_timer=time() #какое время щас в секундах
struct=localtime(start_timer) #загоняем в структуру локального типа
print('\nStarting countdown at:', strftime('%X', struct))
i=10
while i>-1: 
    print(i)
    i-=1
    sleep(1)
end_timer=time()
difference=round(end_timer - start_timer)
print('\nRuntime:', difference, 'Seconds')