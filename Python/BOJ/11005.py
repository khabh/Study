# import sys
# import string
#
# tmp = string.digits + string.ascii_uppercase
#
#
# def convert(num, base):
#     result = ''
#
#     while num > 0:
#         num, mod = divmod(num, base)
#         result += tmp[mod]
#
#     return result[::-1]
#
#
# n, b = map(int, sys.stdin.readline().split())
# if b == 10:
#     print(n)
#     sys.exit()
# print(convert(n, b))

import sys

c = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

n, b = map(int, sys.stdin.readline().split())
ans = ''

while n != 0:
    ans += str(c[n%b])
    n = n // b

print(ans[::-1])
