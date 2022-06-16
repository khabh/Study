import sys
input = sys.stdin.readline

a,b = map(int,input().split())
temp = a
exponent = 1


while temp <= b:
    temp = a * (2 ** exponent)
    