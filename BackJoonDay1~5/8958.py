a=int(input())

for i in range(a):
    b= list(input())
    score= 0
    sum_score =0
    for x in b:
        if x =="O":
            score += 1
            sum_score += score
        else:
            score=0
    print(sum_score)