n = list(map(int, input()))
if 0 in n and sum(n) % 3 == 0:
    n.sort(reverse=True)
    n = list(map(str, n))
    print("".join(n))
else:
    print(-1)
