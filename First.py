# print([i for i in range(2, int(input()) + 1, 2)])

# L = input().split()
# M = input().split()
#
# for i in range(len(L)):
#     print(int(L[i]) + int(M[i]), end =' ')

# S = input().split()
# print('+'.join(S), '=', sum([int(i) for i in S]), sep='')


# 000-000-0000
# 7-000-000-0000
# flag = True
# S = input().split('-')
#
# if len(S) == 4:
#     if len(S[0]) == 1 and S[0] == '7' and len(S[1]) == len(S[2]) == 3 and len(S[3]) == 4:
#         flag = True
#     else:
#         flag = False
# elif len(S) == 3:
#     if len(S[0]) == len(S[1]) == 3 and len(S[2]) == 4:
#         flag = True
#     else:
#         flag = False
# else:
#     flag = False
# for i in S:
#     if not i.isdigit():
#         flag = False
#         break
#
# if flag == False:
#     print('NO')
# else:
#     print('YES')

    # n = input().split("-")
    # c = [len(i) for i in n]
    # if c == [3, 3, 4] and ''.join(n).isdigit():
    #     print("YES")
    # elif c == [1, 3, 3, 4] and ''.join(n).isdigit() and n[0] == '7':
    #     print("YES")
    # else:
    #     print("NO")


# print(max((int(len(i))) for i in input().split()))

# S = input().split()
# for i in input().split():
#     i = i[1:] + i[:1]
#     print(i + 'ки', end=' ')

print(*(i[1:] + i[:1] + 'ки' for i in input().split()))
