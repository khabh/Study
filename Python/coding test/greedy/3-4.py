# 주어진 수 N이 1이 될 때까지 1을 빼거나 K로 N을 나누는 두 과정 중 하나를 선택하여 수행하려고 한다
# 단 두 번째 과정은 완전히 나누어떨어질 때만 선택할 수 있다.


# n, k = map(int, input().split())
# cnt = 0
# while n != 1:
#     if n % k == 0:
#         n = n//k
#     else:
#         n -= 1
#     cnt += 1

# print(cnt)

# 수정
n, k = map(int, input().split())
cnt = 0

while n >= k:
    while n % k != 0:
        n -= 1
        cnt += 1

    n //= k
    cnt += 1

while n > 1:
    n -= 1
    cnt += 1

print(cnt)
