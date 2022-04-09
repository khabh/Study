case=int(input())
for i in range(case):
    candy,sibling=map(int,input().split())
    print("You get %d piece(s) and your dad gets %d piece(s)."%(candy//sibling,candy%sibling))
