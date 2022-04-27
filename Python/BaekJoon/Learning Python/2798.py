n, m = map(int, input().split())
card = list(map(int, input().split()))

card.sort(reverse=True)
array = []

for i in range(0, n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            if card[i]+card[j]+card[k] <= m:
                array.append(card[i]+card[j]+card[k])


print(max(array))
