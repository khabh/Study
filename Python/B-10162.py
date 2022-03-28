time=int(input())

a = time//300
time -= a*300
b = time//60
time -= b*60
c = time//10
if time%10!=0:
    print(-1)
else:
    print(a,b,c)    
