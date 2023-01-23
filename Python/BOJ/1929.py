import sys

n, m = map(int, sys.stdin.readline().split())
primes = [False, False] + [True] * (m - 1)
for i in range(2, m + 1):
    for j in range(2 * i, m + 1, i):
        primes[j] = False

result = filter(lambda x: primes[x], range(n, m + 1))
print(*result, sep='\n')

# 빠른 풀이
n,m=map(int,input().split())

prime_list=[True]*(m+1)
prime_list[0]=False
prime_list[1]=False

for i in range(2,int(m**0.5)+1):
    if prime_list[i]:
        for j in range(i*2,m+1,i):
            prime_list[j]=False
for i in range(n,m+1):
    if prime_list[i]:
        print(i)