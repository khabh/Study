n, k = map(int, input().split())
result = 0

while True:
    target = (n//k)*k
    result += (n-target)
    n = target
    if n < k:
        break
    n //= k
    result += 1
    if n == 1:
        break

result += (n-1)
print(result)
