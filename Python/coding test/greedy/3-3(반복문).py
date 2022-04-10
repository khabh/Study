n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    minValue = 10001

    for i in data:
        minValue = min(i, minValue)
    result = max(minValue, result)

print(result)
