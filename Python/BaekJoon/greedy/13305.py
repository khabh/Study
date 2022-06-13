import sys

n = int(sys.stdin.readline())
distance = list(map(int, sys.stdin.readline().rstrip().split()))
price = list(map(int, sys.stdin.readline().rstrip().split()))
minPrice = price[0]
result = 0

for i in range(n-1):
    minPrice = min(price[i], minPrice)
    result += minPrice * distance[i]

print(result)
