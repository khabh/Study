import sys
input = sys.stdin.readline

t = int(input())
for _ in range (t):
    result = 0
    n = int(input())
    stock = list(map(int,input().split()))
    while True:
        if len(stock) > 0:
          maxValue = max(stock)
        else:
          break
        maxIndex = stock.index(maxValue)
        result += maxValue * maxIndex - sum(stock[:maxIndex])
        if maxIndex == n-1:
            break
        stock = stock[maxIndex+1:]
        
    print(result)       
