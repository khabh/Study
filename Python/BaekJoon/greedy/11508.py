import sys

n = int(sys.stdin.readline())
prices = [0] * n

for i in range(n):
    prices[i] = int(sys.stdin.readline())

prices.sort(reverse=True)
result = sum(prices)

for i in range(2, n, 3):
    result -= prices[i]

print(result)
