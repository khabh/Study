import sys

numbers = [True for _ in range(1000001)]
numbers[0] = numbers[1] = False

for i in range(3, 1001, 2):
    for j in range(i * 3, 1000001, i * 2):
        numbers[j] = False

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    result = False
    for i in range(3, n + 1, 2):
        if numbers[i] and numbers[n - i]:
            print(f'{n} = {i} + {n - i}')
            result = True
            break
    if not result:
        print("Goldbach's conjecture is wrong.")
