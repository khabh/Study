n = int(input())
seat = input()

result = n + 1 - seat.count('L')//2

if result > n:
    result = n
print(result)
