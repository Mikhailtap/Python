podkova=input().split()
max_zn=1
final_list=[]
final_answ=0
if len(podkova)==4: flag1=True
else: flag1=False
flag2=0
for i in range(len(podkova)):
    if podkova[i].isdigit()==True: flag2+=1
if len(podkova)==flag2: flag3=True
else: flag3=False
if flag1==flag3:
    dublicate={}
    for i in podkova:
        if i in dublicate: dublicate[i]+=1
        else: dublicate[i]=1
    for key, value in dublicate.items():
        if value>max_zn: final_list.append(dublicate[key])
    for i in range(len(final_list)):
        final_answ+=final_list[i]-1
    if len(final_list)==0: print(0)
    else: print(final_answ)
else: print('Error')