import sys
input = sys.stdin.readline

numbers = input()
cnt = numbers.count("01") + numbers.count("10")

print((cnt+1)//2)
