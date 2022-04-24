while True:
    n = int(input())
    if n == 0:
        break
    m = 2*n

    a = [False, False]+[True]*(m-1)
    primes = []
    cnt = 0

    for i in range(2, m+1):
        if a[i]:
            primes.append(i)
            for j in range(2*i, m+1, i):
                a[j] = False

    for k in primes:
        if k > n and k <= m:
            cnt += 1

    print(cnt)
