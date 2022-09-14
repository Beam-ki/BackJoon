from ast import In


a= int(input())  #설탕 kg 수
#b는 포대의 
b=0
while a >=0:
    if a % 5 ==0:
        b += (a//5)
        print(b)
        break
    a -= 3
    b += 1
else:
    print(-1)
    