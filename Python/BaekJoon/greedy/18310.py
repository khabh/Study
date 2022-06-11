import sys
input = sys.stdin.readline

n = int(input())
house = list(map(int,input().split()))
house.sort()

total = sum(house)
left = 0
right = total - house[0]
result = right - house[0] * (n - 1)
location = house[0]

for i in range(1,n):
    left += house[i-1]
    right -= house[i]
    distance = house[i] * (2 * i + 1 - n) - left + right
    if distance < result:
        result = distance
        location = house[i]
        
print(location)