import sys
from collections import Counter

read = sys.stdin.readline
read()
cards = Counter(read().split())
read()
print(" ".join(f'{cards[x]}' if x in cards else '0' for x in read().split()))
