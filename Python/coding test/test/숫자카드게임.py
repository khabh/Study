n, m = map(int, input().split())
result = 0
for _ in range(n):
    array = (list(map(int, input().split())))
    result = max(result, min(array))


print(result)
