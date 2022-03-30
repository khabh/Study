a=int(input())
for i in range(a,0,-1):
    print(" "*(a-i)+"*"*(i*2-1))
    
for i in range(2,a+1):
    print(" "*(a-i)+"*"*(i*2-1))
