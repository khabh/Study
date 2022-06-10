import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int,input().split()))
numbers.sort()
totalSum = sum(numbers)
result = totalSum-numbers[0] * (n)
left = 0
right = totalSum - numbers[0]
index = 0

for i in range(1,n):
    left += numbers[i-1]
    right -= numbers[i]
    
    total = numbers[i] * (i-n+i+1) - left + right
    # leftSum =  numbers[i] * i - left
    # rightSum = right - numbers[i] *(n-i-1)
    # total = leftSum + rightSum
    
    if result > total:
        result = total
        index = i

print(numbers[index])