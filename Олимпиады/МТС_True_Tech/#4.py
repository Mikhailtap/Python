import sys
n=input()
if n.isdigit()!=True: print('0')
else:
    n=int(n)
    flag=[]
    flag1=[]
    if 1<=n<=10^5:
        flag2=True
        a=[]
        count=0
        i=0
        sch2=10^5
        for line in sys.stdin:
            if i<n-1:
                a.append(line.rstrip('\n'))
                b=a[i]
                b=str(b)
                if b.isdigit()==True:
                    a[i]=int(b)
                    if 0<=a[i]<=10^6:
                        count=count+(a[i]%2)
                        if (a[i]//2) < sch2:
                            sch2=a[i]//2
                            print(a[i]//2)
                        flag.append(int(1))
                        flag1.append(int(1))
                    else: flag1.append(int(0))
                else: 
                    flag.append(int(0))
                i+=1
                continue
            elif i==n-1:
                a.append(line.rstrip('\n'))
                b=a[i]
                b=str(b)
                if b.isdigit()==True:
                    a[i]=int(b)
                    if 0<=a[i]<=10^6:
                        count=count+(a[i]%2)
                        if (a[i]//2) < sch2:
                            sch2=a[i]//2
                            print(sch2)
                        flag.append(int(1))
                        flag1.append(int(1))
                        break
                    else: 
                        flag1.append(int(0))
                        break
                else: 
                    flag.append(int(0))
                i+=1
                break
            else: break
    else: flag2=False
    if flag2==True:
        for i in range(len(flag)-1):
            flag[i]+=flag[i+1]
        for i in range(len(flag1)-1):
            flag1[i]+=flag1[i+1]
        if len(flag)!=len(a) or len(flag1)!=len(a): flag3=False
        else:
            if count%2==0 or count==0: flag3=True
            else: flag3=False
        if flag3==True: print(sch2)
    else: print('0')