people=[]
for i in range(10):
    minus,plus=map(int,input().split())
    if i!=0:
        people.append(plus-minus+people[i-1])
    else:
        people.append(plus)
    
people.sort()
print(people[-1])
    
