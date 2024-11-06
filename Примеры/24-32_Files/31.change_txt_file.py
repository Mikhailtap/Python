text='the political slogan "workers of the world unite!" is the from the communist manifesto'
#сверху у нас и так все понятно
with open('31.update.txt', 'w') as file: #открыть
    file.write(text) #в файл записывается text
    print('\nfile now closed?:', file.closed)
    #закрыть (автоматически)
#так, это блок для работы с текстом. Открывает и закрывает в конце.
print('file now closed?', file.closed) #проверка
with open('31.update.txt', 'r+') as file:
    text=file.read() #в text записыается из файла
    print('\nstring:', text)
    print('\nposition in file now:', file.tell()) #итого конечная позиция
    position=file.seek(33) #указываем позицию в файле
    print('position in file now:', file.tell())
    file.write('all lands')
    file.seek(59)
    file.write('the tombstone of Karl Marx.')
    file.seek(0)
    text=file.read()
    #все, здесь файл закрывается
print('\nstring:', text)