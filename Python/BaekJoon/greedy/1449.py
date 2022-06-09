import sys
n, l = map(int,sys.stdin.readline().split())
leakPoint = list(map(int,sys.stdin.readline().split()))
leakPoint.sort()
visited = [False] * n
result = 0

for i in range(n):
    if visited[i]:
        continue
    else:
        result += 1
        now = leakPoint[i]
        leakPoint[i] = True
        for j in range (i+1, n):
            if now + l -1 >= leakPoint[j]:
                visited[j] = True
            else:
                break
    
print(result)