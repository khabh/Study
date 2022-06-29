def solution(foodTimes, k):
    if sum(foodTimes) <= k:
        return -1
    last = False
    eatable = [i for i in range(len(foodTimes))]
    eatableCount = len(eatable)
    while not last:
        cycle = min(list(filter(lambda x: x!=0,foodTimes)))
        if k < eatableCount:
            break
        while k - cycle * eatableCount < 0:
            cycle -= 1
            last = True
        k -= cycle * eatableCount   
        removedEatable = eatable[:]
        for i in eatable:
            foodTimes[i] -= cycle
            if foodTimes[i] == 0:
                removedEatable.remove(i)
                eatableCount -= 1
        eatable = removedEatable
    return eatable[k]+1
     
print(solution([3,1,7], 5))