n = int(input())
result = [[0] * 1002 for _ in range(2)]
for i in map(int, input().split()):
    maxIncreaseCount = max(result[0][:i])
    result[0][i] = maxIncreaseCount + 1
    result[1][i] = max(maxIncreaseCount, max(result[1][i + 1:])) + 1
print(max(max(result[0]), max(result[1])))
