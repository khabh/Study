case = int(input())
cnt = 0
for _ in range(case):
    word = input()
    for i in range(len(word)-1):
        if word[i+1] != word[i] and word[i+1] in word[:i]:
            cnt += 1
            break


print(case-cnt)
