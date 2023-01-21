import sys

n = int(input())
numbers = []
for _ in range(n):
    numbers.append(int(sys.stdin.readline()))
numbers.sort()

prevNumber = numbers[0]
result = numbers[0]

maxCount = 0
currentCount = 0
for number in sorted(numbers):
    if number != prevNumber:
        if currentCount > maxCount:
            maxCount = currentCount
            result = prevNumber
        prevNumber = number
        currentCount = 0
    currentCount += 1

if currentCount > maxCount:
    result = numbers[-1]
print(result)

