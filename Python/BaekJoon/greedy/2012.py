import sys
input = sys.stdin.readline

n = int(input())
result = 0
expections = [0] * n

for i in range(n):
    expections[i] = int(input())
expections.sort()

for i in range(1,n-1):
    if expections[i] == expections[i-1]:
        for j in range(i+1,n+1):
            if expections.count(j) == 0:
                result += j - expections[i]
                del expections[i]
                expections.append(j)
                
                
print(result)

# n = int(input())
# result = 0
# expections = [0] * n


# for i in range(n):
#     expections[i] = int(input())

# change = expections[:]
# have = set(expections)
# for num in have:
#     change.remove(num)

    
# for j in range(1,n+1):
#     if not(j in have):
#         minValue = 1e9
#         for i in change:
#             if abs(j - i) < minValue:
#                 minValue = abs(j - i)
#                 changedNum = i
#         change.remove(changedNum)
#         result += minValue
        
# print(result)        

# 등수의 개수를 리스트에 저장?