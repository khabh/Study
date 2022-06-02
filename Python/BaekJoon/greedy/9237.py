n = int(input())
trees = list(map(int, input().split()))
trees.sort(reverse=True)
grown = 0

for i in range(n):
    grown = max(grown, trees[i]+i+1)

print(grown+1)
