case = int(input())
array = []
for i in range(case):
    data = (list(input().split()))
    array.append((data[0], int(data[1])))

array = sorted(array, key=lambda student: student[1])

for i in array:
    print(i[0], end=" ")
