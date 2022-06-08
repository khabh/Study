import sys
n = int(sys.stdin.readline())
students = list(map(int,sys.stdin.readline().split()))
students.sort()
result =  1e9

for i in range (n):
    result = min(students[i]+ students[2*n-1-i],result)
    
print(result)