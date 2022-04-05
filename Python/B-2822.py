score=[]
for _ in range (8):
    score.append(int(input()))
    
compare=score[:]  
score.sort()
print(sum(score[3:]))
for i in range (8):
    if compare[i]>=score[3]:
        print(i+1,end=" ")