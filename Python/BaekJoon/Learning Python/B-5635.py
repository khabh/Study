a=int(input())
lsit=[]
for _ in range(a):
    name, date, month, year=map(str,input().split())
    date,month,year=map(int,(date,month,year))
    lsit.append((year,month,date,name))
    
lsit.sort()
    
print(lsit[-1][3])
print(lsit[0][3])
