numbers = list(map(int, input()))
result = max(numbers[0]*numbers[1], numbers[0] + numbers[1])

for num in numbers[2:]:
    result = max(result * num, result + num)

print(result)
