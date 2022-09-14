word=input().upper()
word1=list(set(word))

cnt=[]
for x in word1:
    cnt1=word.count(x)
    cnt.append(cnt1)

if cnt.count(max(cnt))>1:
    print('?')
else:
    max_index = cnt.index(max(cnt))
    print(word1[max_index])