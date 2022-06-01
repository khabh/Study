import sys
input = sys.stdin.readline


def electCongress(congress):
    if len(member) == 0:
        return 0
    while congress <= member[0]:
        congress += 1
        member[0] -= 1
        if len(member) >= 2 and member[1] > member[0]:
            member.sort(reverse=True)

    return congress - temp


n = int(input())
congress = int(input())
temp = congress
member = []

for _ in range(n-1):
    member.append(int(input()))

member = [x for x in member if x >= congress]
member.sort(reverse=True)
result = electCongress(congress)
print(result)
