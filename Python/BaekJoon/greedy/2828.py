locations = []
result = 0

n, m = map(int, input().split())
j = int(input())

for _ in range(j):
    locations.append(int(input()))

left = 1
for i in locations:
    right = left + m - 1
    target = i
    if target >= left and target <= right:
        continue
    if target > right:
        result += target - right
        left = i - m + 1
    else:
        result += left - target
        left = i


print(result)
