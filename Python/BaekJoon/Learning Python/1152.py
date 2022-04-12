line = input()
word = line.count(" ")+1
if line[0] == " ":
    word -= 1
if line[-1] == " ":
    word -= 1

print(word)
