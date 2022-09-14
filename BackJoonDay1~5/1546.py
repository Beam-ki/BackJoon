a= int(input())
b= list(map(int,(input().split())))
max=max(b)
for i in range(a):
    b[i] = b[i]/max*100
    avg =sum(b)/a
print(avg)

    



# a = int(input())
# b = list(map(int, input().split()))

# max_b = max(b)

# for i in range(a):
#     b[i] = b[i]/max_b*100
#     avg = sum(b)/ a
# print(avg)