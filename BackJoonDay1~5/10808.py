a = int(input())
b = list(map(int, input().split()))
max = b[0]
min = b[0]
for i in range(0, a):
    if int(b[i]) > max:
        max = b[i]
    if int(b[i]) < min:
        min = b[i]
print(min, max)


# a= int(input())
# b= list(map(int,input().split()))
# print(min(b),max(b))

