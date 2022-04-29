def printStar(n):

    if n == 3:
        array = [
                ['*', '*', '*'],
                ['*', ' ', '*'],
                ['*', '*', '*']
        ]
        return array

    array = [[]for i in range(3)]
    for i in range(9):
        if i != 4:
            array[i//3].append(printStar(n//3))
        else:
            array[i//3].append(blank(n))

    return array


def blank(n):
    if n == 3:
        return [' ', ' ', ' ']
    return [[blank(n//3)]for i in range(3)]


# def result(num, array):
#     if num == n:
#         s = ""
#         print("%s" % (s.join(array)), end="")
#     for i in array:
#         result(num*3, i)
#         print()


n = int(input())
star = [[]for _ in range(n)]
k = printStar(n)
print(k)

# result(3, printStar(n))
# for i in k:
#     for j in i:
#         for s in j:
#             print(j)

# for i in range(3):
#     for o in range(3):
#         for j in range(9):
#             s = ""
#             for k in range(27):
#                 s = s.join(k[k][s][i][o][i][:])
#                 print(s)
