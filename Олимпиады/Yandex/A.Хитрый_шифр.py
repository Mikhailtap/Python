def counting(naming):
    count=0
    for al in range(len(alphabet1)):
        for w in range(len(naming)):
            if naming[w]==alphabet1[al]: count+=1
    if count==len(naming): flag=True
    else: flag=False
    return flag

n=input()
if n.isdigit()==True:
    n=int(n)
    if 1<=n<=10000: flag_n=True
    else: flag_n=False
if flag_n:
    alphabet=[chr(i) for i in range(97, 123)] #генерация алфавита по коду
    alphabet1=[chr(i) for i in range(97, 123)]+[chr(i) for i in range(65, 91)]
    for i in range(n):
        lines=input().split(',')
        familia=lines[0]
        imya=lines[1]
        otche=lines[2]
        day=lines[3]
        month=lines[4]
        year=lines[5]       
        if 1<=len(familia)<=15 and 1<=len(imya)<=15 and 1<=len(otche)<=15:
            if familia.isalpha()==imya.isalpha()==otche.isalpha()==True: 
                if counting(familia)==counting(imya)==counting(otche): flag_FIO=True
                else: flag_FIO=False
        if day.isdigit()==month.isdigit()==year.isdigit()==True:
            day=int(day)
            month=int(month)
            year=int(year)
            if 1950<=year<=2021 and 1<=day<=31 and 1<=month<=12: data_correct_firstAttempt=True 
            else: data_correct_firstAttempt=False
            if data_correct_firstAttempt:
                visoc=1948
                if (year-visoc)%4==0: flag_day_visoc=True
                else: flag_day_visoc=False
                if flag_day_visoc==True or flag_day_visoc==False:
                    match month:
                        case 1|3|5|7|8|10|12: data_correct_secondAttempt=True
                        case 2: 
                            if flag_day_visoc==True:
                                if 1<=day<=29: data_correct_secondAttempt=True
                                else: data_correct_secondAttempt=False
                            else:
                                if 1<=day<=28: data_correct_secondAttempt=True
                                else: data_correct_secondAttempt=False
                        case 4|6|9|11:
                            if 1<=day<=30: data_correct_secondAttempt=True
                            else: data_correct_secondAttempt=False
        if flag_FIO and data_correct_secondAttempt:     
            for bukva in range(len(alphabet)):
                if alphabet[bukva]==familia[0].lower():
                    bukva_search=bukva+1
            day=day%10 + day//10
            month=month%10 + month//10
            fio=familia+imya+otche
            fio=len(set(fio))
            final1=fio+(day+month)*64+bukva_search*256
            final1=format(final1, 'X')
            if len(final1)>3:
                final=final1[::-1]
                final=final[:3]
                final=final[::-1]
            elif len(final1)<3:
                count_final=3-len(final1)
                final=''
                for i in range(count_final):
                    final+='0'
                final+=final1
            else: final=final1
        print(final)