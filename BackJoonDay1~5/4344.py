a= int(input())
for x in range(a):
    b=list(map(int,(input().split())))
    avg= sum(b[1:])/b[0]
    cnt=0
    for i in b[1:]:
        if i >avg:
            cnt += 1
    per =(cnt/b[0])*100
    print('%.3f' %per + '%')