Number=int(input())

result=0
for i in range(1,Number+1):
    A=list(map(int,str(i)))
    result=i+sum(A)
    if result==Number:
        print(i)
        break
    if i==Number:
        print(0)
