#bool = True
#if bool:
#    print ('Python in easy steps')
#else:
#    pass

title = '\nPython in easy steps\n'
for char in title:
    print (char, end = ' ')
for char in title:
    if char == 'y':
        print ('*', end = ' ')
        continue
    print (char, end = ' ')
for char in title:
    if char == 'y':
        print ('*', end = ' ')
        pass
    print (char, end = ' ')

'''кароче, pass позволяет интерпретаору обрабатывать все последующие
строки цикла в текущей итерации, а continue - пропускает все остальные
строки в текущей итерации и переходит к следующей'''