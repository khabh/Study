cnt=[]

word=input().upper()
wordList=list(set(word))

for i in wordList:
    cnt.append(word.count(i))
    
if cnt.count(max(cnt))>1:
    print('?')
else:
    print(wordList[(cnt.index(max(cnt)))])