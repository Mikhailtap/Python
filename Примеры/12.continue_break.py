for i in range (1, 4):
    for j in range (1, 4):
        if i==1 and j==1:
            print ('Continue inner loop at i=1 j=1')
            continue
        if i==2 and j==1:
            print('Breaks inner loop at i=2 j=1')
            break
        print ('Running i=', i, 'j=', j)

'''кароче, break - цикл немедленно завершается и пограмма передает управление
следующей инструкции.
for i in range(1, 4):
   for j in range(1, 4):
       print(i, j)
 continue - просто пропускаем одну итерацию цикла'''