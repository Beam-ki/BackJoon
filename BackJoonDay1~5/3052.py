a=[]                     #빈 보따리 생성
for i in range(10):      # 
    b=int(input())       #b라는 보따리에 10개만큼의 자리를 생성
    a.append(b%42)      # a 라는 빈보따리에 b에 들어간 숫자 % 42 한 값(나머지)를 넣음
a = set(a)           #set을이용해 보따리안에있는 중복된 값을 전부제거후 한개만 남김
print(len(a))          #len을 이용해 길이를측정 모두같다면 전부 0으로 1출력 한개가다르다면 2출력



