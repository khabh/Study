n = int(input())
result = [[0, 0]]
for _ in range(n):
    number = int(input())
    result.append([number, number])
for i in range(2, n + 1):
    result[i][0] += result[i - 1][1]
    result[i][1] += max(result[i - 2])
print(max(result[n]))
