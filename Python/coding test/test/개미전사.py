n = int(input())
result = [0] * n
k = list(map(int, input().split()))
result[0] = k[0]
result[1] = max(k[1], k[0])

for i in range(2, n):
    result[i] = k[i] + max(result[:i-1])

print(result[n-1])
