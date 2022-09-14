
list_a=[]
list_b=[]

list_a,list_b=map(list,(input().split()))
list_a[0],list_a[2] = list_a[2],list_a[0]
list_b[0],list_b[2] = list_b[2],list_b[0]
if list_a[0] > list_b[0]:
    a=''.join(list_a)
    print(a)
elif list_a[0] < list_b[0]:
    b=''.join(list_b)
    print(b)
elif list_a[0] == list_b[0] and list_a[1] > list_b[1]:
    a=''.join(list_a)
    print(a)
elif list_a[0] == list_b[0] and list_a[1] < list_b[1]:
    b=''.join(list_b)
    print(b)
elif list_a[0] == list_b[0] and list_a[1] == list_b[1] and list_a[2] > list_b[2]:
    a=''.join(list_a)
    print(a)
else:
    b=''.join(list_b)
    print(b)
