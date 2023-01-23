import sys

n = int(sys.stdin.readline())
a = 2
while a ** 2 <= n:
    if n % a:
        a += 1
        continue
    print(a)
    n //= a
if n > 1:
    print(n)
