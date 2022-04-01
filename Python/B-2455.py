station=[]
for i in range(4):
    minus,plus=map(int,input().split())
    if i==0:
        station.append(plus-minus)
    else:
        station.append(plus-minus+station[i-1])
station.sort()        
print(station[-1])
    

    
