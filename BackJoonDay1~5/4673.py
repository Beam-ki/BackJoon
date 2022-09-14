# a=int(input())
# b=[]
# for i in range(1,10000):
#     while True:
#         i=a+(a//10)+(a%10)
#         i += int(i)


#         i>10000
#         print(i)
#         break


def d(n):
    num = list(str(n))
    asw = n
    for i in range(len(num)):
        asw += int(num[i])
    return asw

SET = list(range(1,10001))
for n in range(1,10001):
    if d(n) in SET:
        SET.remove(d(n))
    
for i in range(len(SET)):
    print(SET[i])