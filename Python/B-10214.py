case=int(input())

for i in range(case):
    a=b=0
    for _ in range(9):
        x,y=map(int,input().split()) 
        a+=x
        b+=y

    if a> b:
            print("Yonsei")
    elif a<b:
            print("Korea")
    else:
            print("Draw")
