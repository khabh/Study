number = int(input())
result = 1
cnt = 0
for i in range(2, number+1):
    result *= i
result = str(result)
for i in result[::-1]:
    if i != '0':
        print(cnt)
        break
    cnt += 1
