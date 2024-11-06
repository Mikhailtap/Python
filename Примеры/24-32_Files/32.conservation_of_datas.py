import os, pickle

if not os.path.isfile('32.pickle.dat'): #если не найден файл
    data=[0, 1]
    data[0]=input('enter topic ')
    data[1]=input('enter series ') #типа в список заносим...
    file=open('32.pickle.dat', 'wb')
    pickle.dump(data, file) #заносим список в файл, преобразовывая его.
    file.close()
else:
    file=open('32.pickle.dat', 'rb')
    data=pickle.load(file)
    file.close()
print('Welcome back to: ' + data[0] + ',' + data[1])