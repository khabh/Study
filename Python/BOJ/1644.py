import sys

N = int(sys.stdin.readline())
primes = [True] * (N + 1)
for i in range(2, int(N ** 0.5) + 1):
    if primes[i]:
        for j in range(i * 2, N + 1, i):
            primes[j] = False
numbers = [i for i in range(2, N + 1) if primes[i]]
result = 0
i = 0
j = 0
count = 0
while 1:
    if result > N:
        result -= numbers[i]
        i += 1
    else:
        if result == N:
            count += 1
        if j == len(numbers):
            break
        result += numbers[j]
        j += 1
print(count)
