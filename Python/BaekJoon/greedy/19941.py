import sys
input = sys.stdin.readline

n, k = map(int,input().split())
table = list(input())
answer = 0

for i in range(n):
    if table[i] == 'P':
        for j in range(max(0,i-k),min(n,i+k+1)):
            if table[j] == 'H':
                table[j] = 0
                answer += 1
                break
            
print(answer)
