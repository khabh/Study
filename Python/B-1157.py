word=list(input())
cnt={}  

for i in range (len(word)):
    if word[i]>'Z':
        word[i]=chr(ord(word[i])-32)
  

 
for j in word:
    if j in cnt:
        cnt[j]+=1
    else:
        cnt[j]=1

maxCount=0
for key in cnt:
    if cnt[key]==cnt[max(cnt)]:
        maxCount+=1
        

if maxCount!=1:
    print('?') 
else:
    print(str(max(cnt)))