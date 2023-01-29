import sys

N, K = map(int, sys.stdin.readline().rstrip().split())
coin = [int(sys.stdin.readline()) for _ in range(N)]
count = 0
for i in coin[::-1]:
    a, K = divmod(K, i)
    count += a
    if K == 0:
        break
print(count)
