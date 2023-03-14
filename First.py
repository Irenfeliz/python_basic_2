s = input()
numbers = s.split()
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
numbers.sort()
print(*numbers)
numbers.sort(reverse=True)
print(*numbers)