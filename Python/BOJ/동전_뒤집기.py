import sys

input = sys.stdin.readline

n = int(input())
coin = [list(input().rstrip()) for _ in range(n)]
flipped_coin = [k[:] for k in coin]
ans = n ** 2

for i in range(n):
    for j in range(n):
        flipped_coin[i][j] = 'T' if flipped_coin[i][j] == 'H' else 'H'

for status in range(1 << n):
    temp = []
    for i in range(n):
        if status & (1 << i):
            temp.append(flipped_coin[i])
        else:
            temp.append(coin[i])

    total = 0
    for i in range(n):
        count = 0
        for j in range(n):
            if temp[j][i] == 'T':
                count += 1
        total += min(count, n - count)
    ans = min(ans, total)
print(ans)
