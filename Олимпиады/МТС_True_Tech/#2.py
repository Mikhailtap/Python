a=input()
if a.isalpha()==True and a.isupper()==True: flag=True
else: flag=False
b='MTS'
if 3<=len(a)<=10000 and flag:
    i=j=0
    while i<len(a) and j<len(b): #реализация перебора без кэширования
        if a[i]==b[j]:
            j+=1
        i+=1
    if j==len(b): print('1')
    else: print('0')
    '''foundM=False
    foundT=False
    foundS=False
    for i in range(len(a)):
        if a[i]=='M' and foundT==foundS==False:
            foundM=True
        if a[i]=='T' and foundM==True and foundS==False:
            foundT=True
        if a[i]=='S' and foundM==foundT==True:
            foundS=True
    if foundM==foundT==foundS==True: print('1')'''
else: print('0')