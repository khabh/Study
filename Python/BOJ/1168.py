import sys

n, k = map(int, sys.stdin.readline().split())
a = [i for i in range(1, n + 1)]
result = []
k -= 1
num = 0
count = n

for i in range(n - 1):
    num += k
    if num > count:
        num %= count
    result.append(a.pop(num))
    count -= 1
result.append(a[0])
print(f'<{str(result)[1:-1]}>')

