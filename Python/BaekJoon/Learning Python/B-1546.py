subject=int(input())
score=list(map(int,input().split()))
score.sort()
for i in range(subject):
    score[i]=score[i]/score[-1]*100
    
    
print(sum(score)/subject)
