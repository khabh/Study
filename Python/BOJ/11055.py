input()
result = [0 for i in range(1001)]
for i in map(int, input().split()):
    result[i] = max(result[:i]) + i
print(max(result))
