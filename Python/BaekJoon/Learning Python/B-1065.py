def find(n):
    numbers=list(str(n))
    if len(numbers)<=2:
        return True
    for i in range (len(numbers)-2):
        if int(numbers[i+1])-int(numbers[i])!=int(numbers[i+2])-int(numbers[i+1]):
            return False
            
    return True
        
        
N=int(input())
cnt=0
for i in range (1,N+1):
    if find(i)==True:
        cnt+=1
        
print(cnt)
