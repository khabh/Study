import sys

n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
sum = len(numbers)
for num in numbers:
    if num == 1:
        sum -= 1
        continue
    for i in range(2, num):
        if num % i == 0:
            sum -= 1
            break

print(sum)
