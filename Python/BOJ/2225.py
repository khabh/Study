import sys

n, k = map(int, input().split())
if k == 1:
    print(1)
    sys.exit()
if k == 2:
    print(n + 1)
    sys.exit()
result = [[i for i in range(1, n + 2)]]
for i in range(1, k - 1):
    temp = [1]
    for j in range(1, n + 1):
        temp.append(temp[j - 1] + result[i - 1][j])
    result.append(temp)
print(result[-1][-1] % 1000000000)
