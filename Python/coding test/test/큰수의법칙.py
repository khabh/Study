n, m, k = map(int, input().split())
num = list(map(int, input().split()))

num.sort()
number1 = num[-1]
number2 = num[-2]

# result = 0

# while True:
#     for i in range(k):
#         if m == 0:
#             break
#         result += number1
#         m -= 1

#     if m == 0:
#         break

#     result += number2
#     m -= 1

# print(result)

count = m//(k+1)*k+m % (k+1)

result = count*number1
result += (m - count)*number2

print(result)
