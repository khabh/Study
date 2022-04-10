# 문제
# 어떤 수와 그 수의 숫자 순서를 뒤집은 수가 일치하는 수를 팰린드롬이라 부른다.
# 예를 들어 79,197과 324,423 등이 팰린드롬 수이다.

# 어떤 수 N (1 ≤ N ≤ 1,000,000)이 주어졌을 때, N보다 크거나 같고,
# 소수이면서 팰린드롬인 수 중에서, 가장 작은 수를 구하는 프로그램을 작성하시오.


import math

number = int(input())


def isPrime(m, n):
    array = [True for i in range(n+1)]
    for i in range(m, int(math.sqrt(n))+1):
        if array[i] == True:
            j = 2
            while i*j <= n:
                array[i*j] = False
                j += 1
    return [i for i in range(2, n+1) if array[i]]


primes = isPrime(31, 1000000)

for i in primes:
    reversedStr = (str(i))[::-1]
    if str(i) == reversedStr:
        print(i)
        break
