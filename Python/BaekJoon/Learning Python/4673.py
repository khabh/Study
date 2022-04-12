allNum = list(i for i in range(1, 10001))
addedNum = []
for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    addedNum.append(i)

result = list(set(allNum).difference(addedNum))
result.sort()
print(*result, sep='\n')
