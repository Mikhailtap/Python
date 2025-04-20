okr=10**4
n=input()
if n.isdigit()==True:
    n=int(n)
    if 1<=n<=100: flag1=True
    else: flag1=False
p=input().split()
flag2=0
sum=0
for i in range(len(p)):
    pr=p[i]
    if pr.isdigit()==True: 
        flag2+=1
        pr=int(pr)
        sum+=pr
if flag1 and n==len(p) and len(p)==flag2:
    nap=sum/n
    nap_Final=round(nap, okr)
    print(nap_Final)
else: print('Error')