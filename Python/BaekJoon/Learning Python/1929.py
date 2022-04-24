n, m = map(int, input().split())

a = [False, False]+[True]*(m-1)
primes = []

for i in range(2, m+1):
    if a[i]:
        primes.append(i)
        for j in range(2*i, m+1, i):
            a[j] = False

for k in range(len(primes)):
    if primes[k] >= n:
        print(primes[k])
