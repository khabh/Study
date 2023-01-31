import sys

N = sys.stdin.readline()
count = 0
sum = 0
for n in sorted(list(map(int, sys.stdin.readline().split()))):
    sum += n
    count += sum
print(count)