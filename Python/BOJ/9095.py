result = [0] * 11
result[1] = 1
result[2] = 2
result[3] = 4
n = int(input())
for i in range(4, 11):
    result[i] = result[i - 3] + result[i - 2] + result[i - 1]
for i in range(n):
    print(result[int(input())])