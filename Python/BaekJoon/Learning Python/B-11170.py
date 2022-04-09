case = int(input())
for _ in range(case):
    cnt = 0
    num1, num2 = map(int, input().split())
    for i in range(num1, num2+1):
        cnt += list(str(i)).count('0')
    print(cnt)
