import sys
import heapq
input = sys.stdin.readline
case = int(input())

for _ in range (case):
    stockInfo = []
    result = 0
    previous = 0
    n = int(input())      
    stockPrice = list(map(int,input().split()))
    for i in range(len(stockPrice)):
        heapq.heappush(stockInfo, (-stockPrice[i],i))
    while stockInfo:
        price, day = heapq.heappop(stockInfo)
        result -= price * (day - previous) + sum(stockPrice[previous:day])
        stockInfo = [x for x in stockInfo if x[1] > day]
        previous = day-1
        heapq.heapify(stockInfo)

    
    print(result)    
    
        

