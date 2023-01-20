# 첫 번째 방법 - 168
import sys

n = int(input())
results = []
numbers = list(map(int, input().split()))
for i in numbers:
    results.append([i, 0, 0])
if n == 1:
    print(results[0][0])
    sys.exit()
if max(numbers) < 0:
    print(max(numbers))
    sys.exit()
results[0][1] = results[0][0]
results[0][2] = 0
for i in range(1, n):
    results[i][1] = max(results[i - 1][:2]) + results[i][0]
    results[i][2] = max(results[i - 1])
print(max(results[n - 1]))

# 두 번째 방법 - 148
n = int(input())
numbers = list(map(int, input().split()))
result = [[0] * 2 for _ in range(n)]

if max(numbers) < 0:
    print(max(numbers))
    sys.exit()
result[0][0] = numbers[0]
for i in range(1, n):
    result[i][0] = max(result[i - 1][0], 0) + numbers[i]
    result[i][1] = max(result[i - 1])
print(max(result[n - 1]))

# 세 번째 방법
n = int(input())
a = list(map(int, input().split()))
sum = [a[0]]
for i in range(len(a) - 1):
    sum.append(max(sum[i] + a[i + 1], a[i + 1]))
print(max(sum))