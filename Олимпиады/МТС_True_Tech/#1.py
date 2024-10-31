import sys 
lines=[]
flag=True
i=0      
for line in sys.stdin:
    if i<2:
        lines.append(line.rstrip('\n'))
        a=lines[i]
        if a.isdigit()==True:
            lines[i]=int(a)
            i+=1
            flag=True
        else:
            i+=3
            flag=False
            print ('Error')
            break
    elif i==2:
        lines.append(line.rstrip('\n'))
        a=lines[i]
        if a.isdigit()==True:
            lines[i]=int(a)
            i+=1
            flag=True
            break
        else:
            i+=3
            flag=False
            print ('Error')
            break
    else: break
if flag==True:
    if 1<=lines[0] and lines[1]<=1000 and 0<=lines[2]<=10000:
        if lines[2]<=100:
            print(lines[0])
        else:
            print((lines[2]-100)*lines[1]+lines[0])
    else: print('Error')  