total = 0
smallest = 100
for i in range(1, 8):
    num = int(input())
    if num % 2 == 1:
        total += num
        if num < smallest:
            smallest = num

if total == 0:
    print(-1)

else:
    print(total)
    print(smallest)
