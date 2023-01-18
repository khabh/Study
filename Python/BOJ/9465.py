case = int(input())
for _ in range(case):
    n = int(input())
    result = [list(map(int, input().split())), list(map(int, input().split()))]
    if n == 1:
        print(max(result[0][0], result[1][0]))
        continue
    result[0][1] += result[1][0]
    result[1][1] += result[0][0]
    for i in range(2, n):
        result[0][i] += max(result[1][i - 1], result[1][i - 2])
        result[1][i] += max(result[0][i - 1], result[0][i - 2])
    print(max(result[1][n - 1], result[0][n - 1]))


