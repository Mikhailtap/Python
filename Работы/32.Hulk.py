n=input()
first='I hate it'
second='I love it'
final=''
if n.isdigit()==True:
    n=int(n)
    if 1<=n<=100: flag1=True
    else: flag1=False
else: print('Error')
if flag1:
    for i in range(1, n+1):
        if i%2==0: final+=second + ' '
        elif i%2!=0: final+=first + ' '
    print(final)
else: print('Error')