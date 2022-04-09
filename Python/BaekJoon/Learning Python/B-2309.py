height=[]
for _ in range (9):
    height.append(int(input()))
height.sort()
total=list(height)
for i in range (8):
    for j in range (i+1,9):
        del total[j]
        del total[i]
        if sum(total)==100:
            break
        else:
            total=list(height)
    if sum(total)==100:
        break        
            
for t in total:
    print(t)
