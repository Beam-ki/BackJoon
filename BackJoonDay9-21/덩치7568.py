people=int(input())
people_list=[]
for i in range(people):
    kg,cm=map(int,input().split())
    people_list.append((kg,cm))

for i in people_list:
    rank = 1
    for j in people_list:
        if i[0]<j[0] and i[1]<j[1]:
            rank +=1
    print(rank,end = " ")