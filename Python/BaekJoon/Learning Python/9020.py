import sys


def findPrime(n):
    array = [True]*n
    m = int(n**0.5)

    for i in range(2, m+1):
        if array[i] == True:
            for j in range(i*2, n, i):
                array[j] = False

    return [i for i in range(2, n) if array[i] == True]


def solve(n):
    prime = findPrime(n)
    j = len(prime)-1
    while prime[j] > n//2:
        j -= 1
    while True:
        if n-prime[j] in prime:
            x, y = prime[j], n-prime[j]
            break

        j -= 1

    return x, y


case = int(sys.stdin.readline().rstrip())
for _ in range(case):
    n = int(sys.stdin.readline())
    x, y = solve(n)
    print(x, y)
