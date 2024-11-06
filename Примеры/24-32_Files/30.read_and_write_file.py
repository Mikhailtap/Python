poem='i never saw a man who looked\n'
poem+='with such a wistful eye\n'
poem+='upon that little tent of blue\n'
poem+='which prisoners call the sky\n'
file=open('30.poem.txt', 'w') #открываем
file.write(poem) #записываем в файл
file.close() #закрываем
file=open('30.poem.txt', 'r')
for line in file: #line - для вывода/ввода линий.
    print(line, end='')
file.close()
file=open('30.poem.txt', 'a')
file.write('(Oscar Wilde)')
file.close()