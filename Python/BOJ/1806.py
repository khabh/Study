import sys

read = sys.stdin.readline
N, S = map(int, read().split())
nums = list(map(int, read().split()))
i = 0
j = 1
result = nums[0]
cnt = 1
answer = 100001
while 1:
    if S <= result:
        if answer > cnt:
            answer = cnt
        result -= nums[i]
        i += 1
        cnt -= 1
    else:
        if j >= N:
            break
        result += nums[j]
        j += 1
        cnt += 1
if answer == 100001:
    print(0)
else:
    print(answer)
