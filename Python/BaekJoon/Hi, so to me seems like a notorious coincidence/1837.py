pq = []
p_q = []
p, k = map(int, input().split())

array = [True for i in range(k+1)]

for i in range(2, int(k**0.5)+1):
    if array[i] == True:
        for j in range(i+i, k, i):
            array[j] = False

result = [i for i in range(2, k) if array[i] == True]
for i in result:
    for j in result:
        if p == i*j:
            print("BAD", min(i, j))

else:
    print("GOOD")
