tc=int(input())
for i in range(tc):

    score=0
    cnt=1
    check=list(input())     

    for i in check:

        if i =='O':  
            score+=cnt
            cnt+=1                       
        else:
            cnt=1        

    print(score)
