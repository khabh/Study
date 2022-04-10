# 주어진 수를 M번 더하고 연속으로 K번을 초과하여 더해질 수 없다


N, M, K = map(int, input().split())
numbers = list(map(int, input().split()))

numbers.sort()
count = (M//(K+1))*K
count += M % (K+1)

total = count*numbers[-1]+(M-count)*numbers[-2]

print(total)
