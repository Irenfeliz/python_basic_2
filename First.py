numbers = [int(input()) for _ in range(int(input()))]
result = []

for num in numbers:
    if num < 0:
        result.append(num)

for num in numbers:
    if num == 0:
        result.append(num)

for num in numbers:
    if num > 0:
        result.append(num)

print(*result, sep='\n')
