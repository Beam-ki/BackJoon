all=0
for i in range(5):
    score=int(input())
    if  score<40 :
        score=40
    all += score
print(all//5)
