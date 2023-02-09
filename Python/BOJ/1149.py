import sys

read = sys.stdin.readline
N = int(read())
price = []
for i in range(N):
    price.append(list(map(int, read().split())))
for i in range(1, N):
    price[i][0] += min(price[i - 1][1], price[i - 1][2])
    price[i][1] += min(price[i - 1][0], price[i - 1][2])
    price[i][2] += min(price[i - 1][0], price[i - 1][1])
print(min(price[N - 1]))
