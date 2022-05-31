array = list(input())
temp = []
result = []


def printAB(cnt):
    if cnt % 2:
        result.append(-1)
        return
    if cnt >= 4:
        result.append(("AAAA" * (cnt//4)))
        if cnt % 4:
            result.append("BB")
    elif cnt == 2:
        result.append("BB")


cnt = 0
for i in range(len(array)):
    if array[i] == 'X':
        cnt += 1

    else:
        if cnt == 0:
            pass
        else:
            printAB(cnt)
            cnt = 0
        result.append(".")
printAB(cnt)

if -1 in result:
    print(-1)
else:
    print("".join(result))
