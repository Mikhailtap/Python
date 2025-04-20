'''def dict_id(dictList): #функция для определения и вывода идентификаторов ракет
    New_id=dictList[0]['id'] #берет первый id в списке словарей
    New_List=[]
    for i in range(len(dictList)):
        if dictList[i]['id']==New_id:
           New_List.append(dictList[i]) #добавляет в новый список значения одного id 
    return New_List'''

'''def DEL_dict_id(dictList): #удаляет наши элементы
    New_id=dictList[0]['id']
    i=0
    while True:
        if len(dictList)==0: break
        if dictList[i]['id']==New_id:
            dictList.pop(i)
        else: break
    return dictList'''

'''def List_id(New_List): #здесь у нас список с идентичным id и выводится сумма по id
    New_List=sorted(New_List, key=lambda x: x['minutes'])
    sum_minutes=0
    i=0
    while True:
        if len(New_List)==0: break
        if New_List[i]['status']=='A' and New_List[i+1]['status']=='B' and (New_List[i+2]['status']=='C' or New_List[i+2]['status']=='S'):
            sum_minutes+=New_List[i+2]['minutes']-New_List[i]['minutes']
            del New_List[0:2+1]
        elif New_List[i]['status']=='A' and New_List[i+1]['status']=='C':
            sum_minutes+=New_List[i+1]['minutes']-New_List[i]['minutes']
            del New_List[0:1+1]
    print(sum_minutes, end=' ')'''

n=input()
if n.isdigit()==True: #количество строк
    n=int(n)
    if 2<=n<=200000: flag_go=True
    else: flag_go=False
if flag_go:
    lines=[] #создаем список наших строк
    flag_line=0
    dictList=[]
    for i in range(n):
        lines=input().split()
        dict_r={}
        day_r=lines[0] #распределяем
        hour_r=lines[1]
        minute_r=lines[2]
        id_r=lines[3]
        status_r=lines[4]
        type_sob=['A', 'B', 'S', 'C']
        if day_r.isdigit()==hour_r.isdigit()==minute_r.isdigit()==id_r.isdigit()==True: #проверка цифр
            day_r=int(day_r)
            hour_r=int(hour_r)
            minute_r=int(minute_r)
            id_r=int(id_r)
            if 1<=day_r<=365 and 0<=hour_r<24 and 0<=minute_r<60 and 0<=id_r<=(10**9): 
                minutes_all=day_r*24*60+hour_r*60+minute_r
                flag_first=True
            else: flag_first=False
        else: flag_first=False
        if len(status_r)==1: #проверка статуса
            if status_r in type_sob: flag_second=True
            else: flag_second=False
        else: flag_second=False
        if flag_first and flag_second: #добавляем в словарь данные
            dict_r['minutes']=minutes_all
            dict_r['id']=id_r
            dict_r['status']=status_r
            dictList.append(dict_r) #добавляем словарь в список
            flagAttempt=True
    dictList=sorted(dictList, key=lambda x: x['id']) #сортировка по возрастанию
    if flagAttempt: #если все проверки прошли успешно, создан список словарей и длина списка равна n
        while True:
            if len(dictList)==0: break
            New_id=dictList[0]['id'] #берет первый id в списке словарей
            New_List=[]
            for i in range(len(dictList)): #создает новый список с одним id
                if dictList[i]['id']==New_id:
                    New_List.append(dictList[i]) #добавляет в новый список значения одного id
            i=0
            while True:
                if len(dictList)==0: break
                if dictList[i]['id']==New_id:
                    dictList.pop(i)
                else: break
            New_List=sorted(New_List, key=lambda x: x['minutes'])
            sum_minutes=0
            i=0
            #проблема - дальше (нужно сократить время и память)
            while True:
                if len(New_List)==0: break
                if New_List[i]['status']=='A' and New_List[i+1]['status']=='B' and (New_List[i+2]['status']=='C' or New_List[i+2]['status']=='S'):
                    sum_minutes+=New_List[i+2]['minutes']-New_List[i]['minutes']
                    del New_List[0:2+1]
                elif New_List[i]['status']=='A' and New_List[i+1]['status']=='C':
                    sum_minutes+=New_List[i+1]['minutes']-New_List[i]['minutes']
                    del New_List[0:1+1]
            print(sum_minutes, end=' ')