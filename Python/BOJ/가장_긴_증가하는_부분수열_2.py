import sys

read = sys.stdin.readline
N = int(read())
numbers = list(map(int, read().split()))
result = [numbers[0]]
for number in numbers[1:]:
    if number > result[-1]:
        result.append(number)
        continue
    start = 0
    end = len(result) - 1
    while start <= end:
        mid = (start + end) // 2
        if result[mid] == number:
            start = mid
            break
        if result[mid] < number:
            start = mid + 1
        else:
            end = mid - 1
    result[start] = number
print(len(result))
