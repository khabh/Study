# import heapq

# def solution(foodTimes, k):
#     foodInfo = []
#     eatableCount = len(foodTimes)
#     for i in range(eatableCount):
#         heapq.heappush(foodInfo, [foodTimes[i], i])    
#     last = False
    
#     while not last:
#         cycle = foodInfo[0][0]
#         if k < eatableCount:
#             break
#         while k < cycle * eatableCount:
#             cycle -= 1
#             last = True
#         k -= cycle * eatableCount
#         for info in foodInfo[:]:
#             foodTimes[info[1]] -= cycle
#             if foodTimes[info[1]] == 0:
#                 eatableCount -= 1
#                 heapq.heappop(foodInfo)
    
#     eatable = sorted(foodInfo, key = lambda x: x[1])
#     return eatable[k][1]+1                    

#         temp = eatable[:]
#         for i in temp:
#             foodTimes[i] -= cycle
#             if foodTimes[i] == 0:
#                 eatableCount -= 1
#                 eatable.remove(i)

def solution(foodTimes, k):
    if sum(foodTimes) <= k:
        return -1
    last = False
    eatableCount = len(foodTimes)
    eatable = [i for i in range(eatableCount)]
    
    while not last:
        cycle = min(list(filter(lambda x: x!=0,foodTimes)))
        if k < eatableCount:
            break
        while k < cycle * eatableCount:
            cycle -= 1
            last = True
        k -= cycle * eatableCount   
        temp = eatable[:]
        for i in temp:
            foodTimes[i] -= cycle
            if foodTimes[i] == 0:
                eatableCount -= 1
                eatable.remove(i)
                
    return eatable[k]+1