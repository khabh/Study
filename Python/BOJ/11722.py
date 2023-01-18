input()
result = [0 for i in range(1002)]
for i in map(int, input().split()):
    result[i] = max(result[i + 1:]) + 1
print(max(result))
