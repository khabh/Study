# 첫째 줄에 N,M,K의 자연수가 주어지며, 각 자연수는 공백으로 구분한다.
# 둘째 줄에 N개의 자연수가 주어진다. 각 자연수는 공백으로 구분한다. 단 가각의 자연수는 1 이상 10,000 이하의 수로 주어진다.
# 입력으로 주어지는 K는 항상 M보다 작거나 같다.
# 주어진 수를 M번 더하고 연속으로 K번을 초과하여 더해질 수 없다

total = cnt = 0

N, M, K = map(int, input().split())

numbers = list(map(int, input().split()))
numbers.sort()

for i in range(M):
    if cnt < K:
        total += numbers[-1]
        cnt += 1
    else:
        total += numbers[-2]
        cnt = 0

print(total)
