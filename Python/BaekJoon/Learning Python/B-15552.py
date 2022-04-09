import sys

turn =int(input())
for i in range(turn):
    a,b=map(int,sys.stdin.readline().split())
    print(a+b)
