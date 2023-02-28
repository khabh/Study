import sys


def dfs(number):
    if len(visit) == N:
        return True
    if not number % 3:
        next_number = number // 3
        if next_number not in visit and next_number in B:
            result.append(next_number)
            visit.add(next_number)
            if dfs(next_number):
                return True
            visit.remove(next_number)
            result.pop()
    next_number = number * 2
    if next_number not in visit and next_number in B:
        result.append(next_number)
        visit.add(next_number)
        if dfs(next_number):
            return True
        visit.remove(next_number)
        result.pop()
    return False


read = sys.stdin.readline
N = int(read())
B = set(map(int, read().split()))
for n in B:
    result = [n]
    visit = {n}
    if dfs(n):
        break
print(*result)
