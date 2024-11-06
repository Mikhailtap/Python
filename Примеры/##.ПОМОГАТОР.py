import os

def search_word(dir_path, text, arr, final_files, flag_files): #проходит по файлам
    os.chdir(dir_path)
    print('\nТекущая директория поиска:\n ', dir_path, '\n')
    files=os.listdir()
    count=0
    for file_name in files:
        abs_dir_path=os.path.abspath(file_name)
        if os.path.isdir(abs_dir_path):
            arr.append(abs_dir_path)
        if os.path.isfile(abs_dir_path):
            if file_name.endswith(".txt") or file_name.endswith(".py"):
                with open(file_name, 'r', encoding='utf-8') as file:
                    if text in file.read():
                        #final_dir_path=os.path.abspath(file_name)
                        final_files.append(file_name)
                        #print('FINAL', final_dir_path)
                        count+=1
                        flag_files=True
    if count==0: 
        print('No such file in the directory')
        flag_files=False
    return final_files, flag_files

def IO(dir_path, text, final_files, flag_files): #выводит все на экран
    arr=[]
    search_word(dir_path, text, arr, final_files, flag_files)
    if flag_files:
        print('В директории со словом "', text, '" обнаружены следующие файлы:\n')
        for i in range(len(final_files)):
            print(final_files[i])
    print('\nОбнаружены следующие папки: ')
    close=True
    while close==True:
        print('0', '\tClose the program\n')
        for i in enumerate(arr, 1):
            print(i, '\n')
        folder=int(input('Введите тот порядковый номер, который хотите просмотреть: '))
        if folder==0: 
            close=False
            break
        dir_path=arr[folder-1]
        final_files=[]
        IO(dir_path, text, final_files, flag_files)
        break
    pass

dir_path=r'C:\Михаил\Программирование\Python\Примеры'
print('\nDo you want to change the directory?  Y/N')
print('Directory is: ', dir_path)
choice=input()
if choice==('Y' or 'y'):
    dir_path1=input('Please, enter the new absolutely directory:\n')
    dir_path=os.path.join(dir_path1)
text=input('Please, enter the word: ')    
arr=[]
final_files=[]
flag=True

IO(dir_path, text, final_files, flag)