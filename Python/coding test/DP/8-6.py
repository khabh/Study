n = int(input())
d = list(map(int, input().split()))
d[2] = d[2]+d[0]

for i in range(3, n):
    d[i] += max(d[:i-1])

print(max(d))
