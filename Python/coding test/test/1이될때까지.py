n, k = map(int, input().split())
count = 0

while n >= k:
    if n % k != 0:
        count += n % k
        n = (n//k)*k
    else:
        n = n // k
        count += 1

count += n-1


print(count)
