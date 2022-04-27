def printStar(n):

    if n > 3:

        for i in range(n//3):
            printStar(n/3)
        for k in range(n//3):
            print('*'*(n//3)+' '*(n//3)+'*'*(n//3))
        for j in range(n//3):
            print('*'*n)


n = int(input())
printStar(n)
