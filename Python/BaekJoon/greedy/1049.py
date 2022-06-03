n, m = map(int, input().split())
pack = []
one = []
for _ in range(m):
    a, b = map(int, input().split())
    pack.append(a)
    one.append(b)

price1 = min(one)
price6 = min(pack)

if price1 * 6 <= price6:
    print(price1 * n)
else:
    print(min((n//6)*price6 + (n % 6)*price1, ((n//6)+1)*price6))
