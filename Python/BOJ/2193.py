n = int(input())
results = [[0] * 2 for _ in range(n + 1)]
results[1][0] = 0
results[1][1] = 1

for i in range(2, n + 1):
    results[i][0] = results[i - 1][0] + results[i - 1][1]
    results[i][1] = results[i - 1][0]

print(results[n][0] + results[n][1])
