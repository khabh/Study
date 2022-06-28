import sys
input = sys.stdin.readline

n,m = map(int,input().split())
balls = list(map(int,input().split()))

result = 0
for i in range(n-1):
    result += len(list(filter(lambda x: x!= balls[i],balls[i+1:] )))

print(result)

# 두 번째 풀이

arr = [0] * 11
for ball in balls:
    arr[ball] += 1
    
for i in range(1,m+1):
    n -= arr[i]
    result += arr[i] * n