import sys

n, m = map(int, sys.stdin.readline().split())
price = [0] * m
result = 0
for i in range(m):
    price[i] = int(sys.stdin.readline())
price.sort(reverse=True)

for j in range(m):
    total = price[j] * min((j+1), n)
    if total >= result:
        result = total
        endPrice = price[j]


print(endPrice, result)
