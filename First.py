# keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
# new_keywords = [i[1:] for i in keywords]
# print(new_keywords)

# keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
# lengths = [len(i) for i in keywords]
# print(lengths)

# keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
# new_keywords = [i for i in keywords if len(i) > 4]
# print(new_keywords)

# # от 100 до 1000
# palindromes = [i for i in range(100, 1001) if i // 100 == i % 10]
# print(palindromes)

# n = int(input())
# numbers = [i**2 for i in range(1, n + 1)]
# print(*numbers, sep='\n')

# print(*[i ** 2 for i in range(1, int(input()) + 1)], sep='\n')

# print(*[int(i) ** 3 for i in input().split()])

# print(*input().split(), sep='\n')

# print(*[i for i in input() if i in '0123456789'], sep='')
# print(*(i for i in input() if i.isdigit()), sep='')

print(*(int(i)**2 for i in input().split() if int(i) % 2 == 0 and int(i)**2 % 10 != 4))