first_num=input()
second_num=input()
if len(first_num)<=100 and len(second_num)<=100: flag=True
else: flag=False
if flag:
    string=[]
    final=''
    s=len(first_num)
    i=0
    while i<s:
        if first_num[i]==second_num[i]:
            string.append('0')
        elif first_num[i]!=second_num[i]:
            string.append('1')
        i+=1
    for i in string:
        final+=i
    print(final)
else: print('Error')