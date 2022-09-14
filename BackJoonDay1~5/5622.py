# word=input()
# A,B,C=2,2,2
# D,E,F=3,3,3
# G,H,I=4,4,4
# J,K,L=5,5,5
# M,N,O=6,6,6
# P,Q,R,S=7,7,7,7
# T,U,V=8,8,8
# W,X,Y,Z=9,9,9,9
# print(int(word))


alpabet_list = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
word = input()

time = 0
for unit in alpabet_list :  
    for i in unit:  # alpabet 리스트에서 각 요소를 꺼내서 한글자씩 분리
        for x in word :  # 입력받은 문자를 하나씩 분리
            if i == x :  # 두 알파벳이 같으면
                time += alpabet_list.index(unit) +3  # time = time + index +3
print(time)

10

