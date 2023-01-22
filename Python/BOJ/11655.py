import sys

n = list(sys.stdin.readline().rstrip('\n'))

for i in range(len(n)):
    if not n[i].isalpha():
        continue
    alpha = ord(n[i])
    if 65 <= alpha <= 90:
        n[i] = chr((alpha - 52) % 26 + 65)
        continue
    n[i] = chr((alpha - 84) % 26 + 97)

print(''.join(n))
