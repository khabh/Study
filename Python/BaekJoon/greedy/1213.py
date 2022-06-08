import sys
name = list(sys.stdin.readline().rstrip())

def makeName():
    odd = list(set(name))
    odd.sort()

    mid = []
    right = []
    for i in range(len(odd)):
        alpha = name.count(odd[i])
        right.append(odd[i] * (alpha//2))
        
        if alpha % 2:
            if mid:
                print('I\'m Sorry Hansoo')
                return
            else:
                mid.append(odd[i])

        
    left = right[::-1]
    result = right + mid + left
    print("".join(result))
    
makeName()