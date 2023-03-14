# s = input()
# print(*s.split(), sep='\n')

# s = input()
# l = s.split()
# for i in range(len(l)):
#     print(l[i][0] + '.', end='')

# s = input()
# l = s.split('\\')
# print(*l, sep='\n')

# s = input()
# l = s.split()
# for i in l:
#     print('+' * int(i))

# s = input()
# l = s.split('.')
# for i in range(len(l)):
#     l[i] = int(l[i])
#     if 0 <= l[i] <= 255:
#         flag = True
#     else:
#         flag = False
#         break
# if flag:
#     print('ДА')
# else:
#     print('НЕТ')

# s = input()
# r = input()
# print(r.join(s))

s = input()
l = s.split()
count = 0
for i in range(len(l)):
    for j in range(i+1, len(l)):
        if l[i] == l[j]:
            count += 1
print(count)