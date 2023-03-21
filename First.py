# def get_middle_point(x1, y1, x2, y2):
#     return (x1 + x2) / 2, (y1 + y2) / 2
#
# print(*get_middle_point(0, 0, 10, 0))
# print(*get_middle_point(1, 5, 8, 3))
# import math
#
#
# def get_circle(radius):
#     return 2 * math.pi * radius, math.pi * radius ** 2
#
#
# print(get_circle(1))
# print(get_circle(1.5))

# def solve(a, b, c):
#     x1 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
#     x2 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
#     if x2 >= x1:
#         return x1, x2
#     else:
#         return x2, x1
#
# print(solve(1, -4, -5))
# print(solve(-2, 7, -5))
# print(solve(1, 2, 1))

# def draw_triangle():
#     i = 7
#     for j in range(1, 16, 2):
#         print(' ' * i, '*' * j, sep='')
#         i -= 1
#
# draw_triangle()

# def get_shipping_cost(quantity):
#     return 1000 + 120 * (quantity -1)
#
# print(get_shipping_cost(1))
# print(get_shipping_cost(3))

# def compute_binom(n, k):
#     n_factorial = 1
#     k_factorial = 1
#     nk_factorial = 1
#     for i in range(1, n + 1):
#         n_factorial *= i
#     for j in range(1, k + 1):
#         k_factorial *= j
#     for c in range(1, n - k + 1):
#         nk_factorial *= c
#     return int(n_factorial / (k_factorial * nk_factorial))
#
# print(compute_binom(64, 7))

# def number_to_words(num):
#     list_1 = [' ', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять']
#     list_11 = [' ', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать',
#                'восемнадцать', 'девятнадцать']
#     list_21 = [' ', ' ', 'двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']
#     if 1 <= num <= 10:
#         return list_1[num]
#     if 11 <= num <= 19:
#         return list_11[num % 10]
#     if 20 <= num <= 99:
#         return list_21[num // 10] + ' ' + list_1[num % 10]
#
# print(number_to_words(7))
# print(number_to_words(17))
# print(number_to_words(85))
# print(number_to_words(99))

# def get_month(language, number):
#     lng_ru = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь',
#               'декабрь']
#     lng_en = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october',
#               'november', 'december']
#     if language == 'ru':
#         return lng_ru[number - 1]
#     if language == 'en':
#         return lng_en[number - 1]
#
# print(get_month('ru', 1))
# print(get_month('ru', 12))
# print(get_month('en', 1))
# print(get_month('en', 10))

# def is_magic(date):
#     d = date.split('.')
#     if int(d[0]) * int(d[1]) == int(d[2][2:4]):
#         return True
#     else:
#         return False
#
# print(is_magic('10.09.1990'))
# print(is_magic('03.11.2033'))

def is_pangram(text):
    s = text.replace(' ', '').lower()
    l = []
    li = []
    for i in s:
        if ord(i) in range(97, 123):
            l += [ord(i)]
    [li.append(x) for x in l if x not in li]
    if len(li) == 26:
        return True
    else:
        return False


print(is_pangram('Jackdaws love my big sphinx of quartz'))
print(is_pangram('The jay pig fox zebra and my wolves quack'))
print(is_pangram('Hello world'))