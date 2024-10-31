import sys
n=input()
if n.isdigit()!=True: print('0')
else:
    n=int(n)
    flag=[]
    flag1=[]
    if 1<=n<=1000:
        a=[]
        count=0
        i=0
        for line in sys.stdin:
            print('i1', i)
            if i<n-1:
                print('i2', i)
                a.append(line.rstrip('\n'))
                print('a', a)
                b=a[i]
                b=str(b)
                print('bstr', b)
                if b.isdigit()==True:
                    print('type(b)', type(b))
                    print('b', b)
                    a[i]=int(b)
                    if 0<=a[i]<=100000000:
                        count=count+(a[i]%2)
                        print('a[i]', a[i])
                        print('type(a[i])', type(a[i]))
                        flag.append(int(1))
                        print('flag', flag)
                        flag1.append(int(1))
                        print('flag1', flag1)
                    else: flag1.append(int(0))
                else: 
                    flag.append(int(0))
                    print('flag', flag)
                i+=1
                print('i3', i)
                continue
            elif i==n-1:
                print('i4', i)
                a.append(line.rstrip('\n'))
                print('a', a)
                b=a[i]
                b=str(b)
                print('bstr', b)
                if b.isdigit()==True:
                    print('type(b)', type(b))
                    print('b', b)
                    a[i]=int(b)
                    if 0<=a[i]<=100000000:
                        count=count+(a[i]%2)
                        print('a[i]', a[i])
                        print('type(a[i])', type(a[i]))
                        flag.append(int(1))
                        flag1.append(int(1))
                        print('flag', flag)
                        print('flag1', flag1)
                        break
                    else: 
                        flag1.append(int(0))
                        break
                else: 
                    flag.append(int(0))
                    print('flag', flag)
                i+=1
                print('i5', i)
                break
            else: break
        for i in range(len(flag)-1):
            flag[i]+=flag[i+1]
        for i in range(len(flag1)-1):
            flag1[i]+=flag1[i+1]
        if len(flag)!=len(a) or len(flag1)!=len(a): print('0')
        else:
            if count%2==0 or count==0: print('1')
            else: print('0')
    else: print('0')
    #print(a)