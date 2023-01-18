n = int(input())
result = [[]]
for i in range(n):
    result[0].append(int(input()))
result.append(result[0][:])
result.append([0] * n)
if n <= 2:
    print(sum(result[0]))
else:
    result[0][1] += result[0][0]
    result[2][1] = result[0][0]
    for i in range(2, n):
        result[0][i] += result[1][i - 1]
        result[1][i] += max(result[0][i - 2], result[2][i - 1])
        result[2][i] = max(result[0][i - 1], result[1][i - 1], result[2][i - 1])
    print(max(result[0][n - 1], result[1][n - 1], result[2][n - 1]))
