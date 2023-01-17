# numberCount = int(input())
# number = int(input())
# sum = 0
#
# for i in range(numberCount):
#     sum += number % 10
#     number = int(number / 10)
#
# print(sum)

case = int(input())
numbers = list(input())
total = 0
for i in range(case):
    total += int(numbers[i])
print(total)


