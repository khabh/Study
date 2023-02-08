n, m, *a = map(int, open(0).read().split())
i = c = 0
j = 1
s = a[0]
while 1:
    if s < m:
        if j < n:
            s += a[j]
            j += 1
        else:
            break
    else:
        if s == m:
            c += 1
        s -= a[i]
        i += 1
print(c)
