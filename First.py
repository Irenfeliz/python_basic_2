# n = int(input())
# l = []
# for _ in range(n):
#     k = input()
#     l.extend(k)
# print(l)

# numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]
# sum = 0
# for num in numbers:
#     sum += num ** 2
# print(sum)

# n = int(input())
# numbers = []
# l = []
# for _ in range(n):
#     x = int(input())
#     numbers.append(x)
#     l.append(x**2 + 2*x + 1)
#
# print(*numbers, sep='\n')
# print()
# print(*l, sep='\n')

# n = int(input())
# numbers = []
# newnumbers = []
#
# for _ in range(n):
#     x = int(input())
#     numbers.append(x)
#
# for num in numbers:
#     if num != max(numbers) and num != min(numbers):
#         newnumbers.append(num)
#
# print(*newnumbers, sep='\n')

# n = int(input())
# strings = []
#
# for _ in range(n):
#     s = input()
#     if strings.count(s) < 1:
#         strings.append(s)
# print(strings)

# n = int(input())
# strings = []
#
# for _ in range(n):
#     s = input()
#     strings.append(s)
#
# search = input()
#
# for str in strings:
#     if search.lower() in str.lower():
#         print(str)

n = int(input())
strings = []
searches = []
l = []
results = []

for _ in range(n):
    ns = input()
    strings.append(ns)

k = int(input())

for _ in range(k):
    ks = input()
    searches.append(ks)

for srch in searches:
    for str in strings:
        if srch.lower() in str.lower():
            l.append(str)

for result in l:
    if l.count(result) == k:
        results.append(result)
    if l.count(result) > 1:
        l.remove(result)

print(*results, sep='\n')
