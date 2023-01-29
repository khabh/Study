import sys

sys.stdin.readline()
result = []
A = sorted(list(map(int, sys.stdin.readline().split())))
B = sorted(list(map(int, sys.stdin.readline().split())))
maxI = len(A) - 1
maxJ = len(B) - 1
i = j = 0
while True:
    if A[i] <= B[j]:
        result.append(A[i])
        i += 1
        if i > maxI:
            for x in B[j:]:
                result.append(x)
            break
    else:
        result.append(B[j])
        j += 1
        if j > maxJ:
            for x in A[i:]:
                result.append(x)
            break

print(*result, sep=" ")


sys.stdin.readline()
print(*sorted(list(map(int, sys.stdin.readline().split() + sys.stdin.readline().split()))), sep=" ")
