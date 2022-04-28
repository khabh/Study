# num = int(input())
# array = [0, 666, 1666]

# for i in range(3, num+1):
#     number = array[i-1]
#     numberStr = str(number)
#     index6 = numberStr.find('666')

#     if index6 != len(numberStr)-3:
#         if (array[i-1]) % 10 != 9:
#             array.append(int(array[i-1])+1)
#         else:
#             array.append(2*(10**(len(str(array[i-11]))-1))+array[i-11])
#     elif numberStr[index6-1] == '5':
#         array.append(int(numberStr[0:index6-1]+'6660'+numberStr[index6+3:]))
#     else:
#         if numberStr[:index6] != '':
#             array.append(
#                 int(str(int(numberStr[:index6])+1)+'666'+numberStr[index6+3:]))
#         else:
#             array.append(
#                 int('666'+numberStr[index6+3:]))


# print(array)

num = int(input())
array = []
i = 666

while len(array) < num:
    if '666' in str(i):
        array.append(i)

    i += 1

print(array[-1])
