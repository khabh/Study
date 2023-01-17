number = int(input())
results = []
for i in range(1, number):
    result = i * '*' + ' ' * ((number - i) * 2) + i * '*'
    print(result)
    results.append(result)
print(number * 2 * '*')
for i in range(number - 1):
    print(results.pop())

