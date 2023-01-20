n = int(input())
result = [i for i in range(n + 1)]
square = [i * i for i in range(1, 317)]
for i in range(1, n + 1):
    for j in square:
        if j > i:
            break
        result[i] = min(result[i], result[i - j] + 1)
print(result[n])
