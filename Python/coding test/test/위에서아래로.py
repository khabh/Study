case = int(input())
array = []
for i in range(case):
    array.append(int(input()))

array = sorted(array, reverse=True)

for i in array:
    print(i, end=" ")
