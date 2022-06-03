import sys
input = sys.stdin.readline

N, K = map(int, input().rstrip().split())

minTotal = K*(K+1) // 2

if minTotal > N:
    print(-1)
elif (N - minTotal) % K == 0:
    print(K-1)
else:
    print(K)
