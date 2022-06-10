import sys
input = sys.stdin.readline

n, m = map(int,input().split())
result = []
cnt = 0
use = 0
for _ in range (n):
  p, l = map(int,input().split())
  mileage = list(map(int,input().split()))
  mileage.sort(reverse = True)
  if p >=  l:
    result.append(mileage[l-1])      
  else:
    result.append(1)
result.sort()

for mileage in result:
  if use + mileage <= m:
    use += mileage
    cnt +=1
  else:
    break

print(cnt)