case = int(input())
result = [[0]*case for i in range(case)]
result[0][0] = 1
array = []

for _ in range(case):
    array.append(list(map(int, input().split())))

for i in range(case):
    for j in range(case):
        if i == case-1 and j == case-1:
            print(result[i][j])
            break
        if i+array[i][j] <= case-1:
            result[i+array[i][j]][j] += result[i][j]

        if j+array[i][j] <= case-1:
            result[i][j+array[i][j]] += result[i][j]
