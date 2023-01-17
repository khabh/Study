number = int(input()) - 1
print(number * ' ' + '*')
for i in range(1, number):
    print(' ' * (number - i) + (' ' * (i * 2 - 1)).join('**'))
number += 1
if number > 1:
    print('*' * (number * 2 - 1))