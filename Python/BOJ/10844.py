n = int(input())
results = [[0] * 10 for _ in range(n + 1)]
for i in range(1, 10):
    results[1][i] = 1
for i in range(2, n + 1):
    for j in range(10):
        if j == 0:
            results[i][0] = results[i - 1][1]
        elif j == 9:
            results[i][j] = results[i - 1][8]
        else:
            results[i][j] = results[i - 1][j - 1] + results[i - 1][j + 1]

print(sum(results[n]) % 1000000000)
