# def is_valid_triangle(side1, side2, side3):
#     if side1 + side2 > side3 and side2 + side3 > side1 and side1 + side3 > side2:
#         return True
#     else:
#         return False
#
# # a, b, c = int(input()), int(input()), int(input())
# # print(is_valid_triangle(a, b, c))
# print(is_valid_triangle(2, 2, 2))
# print(is_valid_triangle(2, 3, 10))
# print(is_valid_triangle(3, 4, 5))

# def is_prime(num):
#     if num == 1:
#         return False
#     for i in range(2, num):
#         if num % i == 0:
#             return False
#     return True
#
# print(is_prime(1))
# print(is_prime(17))
# print(is_prime(101))


# Еще одно решение - покороче
# def is_prime(num):
#     if num == 1:
#         return False
#     for i in range(2, num):
#         if num % i == 0:
#             return False
#     return True
#
# # n = int(input())
# # print(is_prime(n))
#
# def get_next_prime(num):
#     for i in range(num + 1, num + 100):
#         if is_prime(i):
#             return i
#
#
# print(get_next_prime(1000))
# print(get_next_prime(2000))
# print(get_next_prime(97001))


# его длина не менее 8 символов;
# он содержит как минимум одну заглавную букву (верхний регистр);
# он содержит как минимум одну строчную букву (нижний регистр);
# он содержит хотя бы одну цифру.
# def is_password_good(password):
#     flag1 = flag2 = flag3 = False
#     if len(password) < 8:
#         return False
#     for i in range(len(password)):
#         if password[i].isupper():
#             flag1 = True
#             continue
#         elif password[i].islower():
#             flag2 = True
#             continue
#         elif password[i].isdigit():
#             flag3 = True
#             continue
#     if flag1 == flag2 == flag3 == True:
#         return True
#     else:
#         return False
#
# # txt = input()
# # print(is_password_good(txt))
# print(is_password_good('aaAA12qqp'))
# print(is_password_good('aa13AN'))
# print(is_password_good('aaaaaaaaaaaaa'))
# print(is_password_good('AAAAAAAAAAA'))


# def is_one_away(word1, word2):
#     count = 0
#     if len(word1) != len(word2):
#         return False
#     for i in range(len(word1)):
#         if word1[i] != word2[i]:
#             count += 1
#     if count == 1:
#         return True
#     else:
#         return False
#
# print(is_one_away('bike', 'hike'))
# print(is_one_away('water', 'wafer'))
# print(is_one_away('abcd', 'abpo'))
# print(is_one_away('abcd', 'abcde'))

# def is_palindrome(text):
#     TEXT = [text[i].lower() for i in range(len(text)) if text[i].isalpha()]
#     TEXT_reverse = [text[i].lower() for i in range(len(text)-1,-1,-1) if text[i].isalpha()]
#     if TEXT == TEXT_reverse:
#         return True
#     else:
#         return False
#
#     # решение покороче
#     # l = [i.lower() for i in text if i.isalpha()]
#     # return l == l[::-1]
#
# #
# print(is_palindrome('А роза упала на лапу Азора.'))
# print(is_palindrome('Gabler Ruby - burrel bag!'))
# print(is_palindrome('BEEGEEK'))

# def is_prime(num):
#     if num == 1:
#         return False
#     for i in range(2, num // 2 + 1):
#         if num % i == 0:
#             return False
#     return True
# def is_palindrome(num):
#     l = [i for i in num if i.isdigit()]
#     return l == l[::-1]
# def is_valid_password(password):
#     flag1 = flag2 = flag3 = False
#     password_list = password.split(':')
#     if len(password_list) != 3:
#         return False
#     if is_palindrome(password_list[0]):
#         flag1 = True
#     if is_prime(int(password_list[1])):
#         flag2 = True
#     if int(password_list[2]) % 2 == 0:
#         flag3 = True
#     return flag1 and flag2 and flag3
# #
# print(is_valid_password('1221:101:22'))
# print(is_valid_password('565:30:50'))
# print(is_valid_password('112:7:9'))
# print(is_valid_password('1221:101:22:22'))

# def is_correct_bracket(text):
#     # l = [i for i in text]
#     # while len(l) > 1:
#     #     if l.count('(') != l.count(')'):
#     #         return False
#     #     if l[0] != '(':
#     #         return False
#     #     if l[-1] != ')':
#     #         return False
#     #     for i in range(len(l)):
#     #         if i + 1 >= len(l):
#     #             break
#     #         if l[i] + l[i + 1] == '()':
#     #             del l[i: i + 2]
#     # return True
#     count = 0
#     for i in text:
#         if i == '(':
#             count += 1
#         elif i == ')':
#             count -= 1
#         if count < 0:
#             return False
#     return count == 0
#
# txt = input()
# print(is_correct_bracket(txt))

def convert_to_python_case(text):
    for i in text:
        if i.isupper():
            text = text.replace(i, '_' + i.lower())
    return text[1:]

print(convert_to_python_case('MyMethodMhatMoMomething'))
print(convert_to_python_case('IsPrimeNumber'))

