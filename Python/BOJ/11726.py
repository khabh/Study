n = int(input())
if n < 3:
    print(n)
else:
    result = [0] * (n + 1)
    result[1] = 1
    result[2] = 2
    for i in range(3, n + 1):
        result[i] = result[i - 1] + result[i - 2]
    print(result[n] % 10007)
