# # объявление функции
# def get_days(month):
#     if month in (1, 3, 5, 7, 8, 10, 12):
#         return 31
#     elif month == 2:
#         return 28
#     else:
#         return 30
# # считываем данные
# num = int(input())
#
# # вызываем функцию
# print(get_days(num))

# def get_factors(num):
#     return [i for i in range(1, num + 1) if num % i == 0]
# n = int(input())
# print(get_factors(n))
# def number_of_factors(num):
#     return len(get_factors(num))
# print(number_of_factors(n))

# def find_all(target, symbol):
#     return [i for i in range(len(target)) if target[i] == symbol]
#
# s = input()
# char = input()
#
# print(find_all(s, char))

# def merge(list1, list2):
#     return sorted(list1 + list2)
#
# print(merge([1, 2, 3], [5, 6, 7, 8]))
# print(merge([1, 7, 10, 16], [5, 6, 13, 20]))

n = int(input())
s = [input().split() for _ in range(n)]

def quick_merge(n, s):
    l = []
    for i in s:
        l += i
    return print(*sorted([int(i) for i in l]))

quick_merge(n, s)