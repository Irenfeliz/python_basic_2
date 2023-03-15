# def draw_box():
#     print('*' * 10)
#     for _ in range(12):
#         print('*', ' ' * 8, '*', sep='')
#     print('*' * 10)
#
# draw_box()

# def draw_triangle():
#     for i in range(1, 11):
#         print('*' * i)
#
# draw_triangle()

# def draw_triangle(fill, base):
#     for i in range(1, base //2 +1):
#             print(fill * i)
#     for k in range(base//2 + 1, 0, -1):
#         print(fill * k)
#
# fill = input()
# base = int(input())
# draw_triangle(fill, base)

# def print_fio(name, surname, patronymic):
#     print(surname[0].upper() + name[0].upper() + patronymic[0].upper())
#
#
# name, surname, patronymic = input(), input(), input()
# print_fio(name, surname, patronymic)

def print_digit_sum(num):
    print(sum(int(i) for i in str(num)))
n = int(input())
print_digit_sum(n)