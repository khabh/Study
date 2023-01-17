n = int(input())
if n == 1:
    print(1)
elif n == 2:
    print(3)
else:
    result = [0] * (n + 1)
    result[1] = 1
    result[2] = 3
    for i in range(3, n + 1):
        result[i] = result[i - 1] + result[i - 2] * 2
    print(result[n] % 10007)
