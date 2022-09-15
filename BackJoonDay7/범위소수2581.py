a =int(input())
b =int(input())
c=[]

for i in range(a,b+1):
    if i ==1:
        pass
    elif i ==2:
        c.append(i)
    else:
        for j in range(2,i):
            if i %j==0:
                break
            elif j==i-1:
                c.append(i)
if len(c)==0:
    print('-1')
else:
    print(sum(c))
    print(min(c))
