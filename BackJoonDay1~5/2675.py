


Number=int(input())

for x in range(Number):
    cnt,word =input().split()
    for _ in word:
        print(_*int(cnt),end='')
    print()
