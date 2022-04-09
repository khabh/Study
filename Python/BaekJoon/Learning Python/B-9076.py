test=int(input())
for _ in range (test):
    score=list(map(int,input().split()))
    score.sort()
    if score[4]-score[1]>=4:
        print("KIN")
    else:
        print(sum(score[1:4]))
