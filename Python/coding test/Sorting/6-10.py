case = int(input())
array = []
for _ in range(case):
    array.append(int(input()))

array = sorted(array, reverse=True)

for i in array:
    print(i, end=" ")
