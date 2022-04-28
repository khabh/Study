num = int(input())
cnt = 0

for i in range(1, num+1):
    array = []
    number = i
    while True:
        if number < 10 and number > 0:
            array.append(number)
            break
        else:
            array.append(number % 10)
            number = number//10

    if sum(array)+i == num:
        print(i)
        cnt = 1
        break

if cnt == 0:
    print(0)
