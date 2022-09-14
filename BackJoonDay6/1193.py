X=int(input())

line=1
while X>line:
    X-=line
    line+=1
    
if line%2==0:
    a=X
    b=line-X+1
else:
    a=line-X+1
    b=X
    
print(a, '/', b, sep='')










    #1번은 분모가1
    #2번은 분모가2로시작 +1/-1 두번
    #5번은 분모가 5로시작 +1/-1 5번
    #...
    #.n번은 분모가 n으로 시작 +1/-1을 n번

