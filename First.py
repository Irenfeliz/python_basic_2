numbers = input().split()
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
minimum = min(numbers)
maximum = max(numbers)
minimum_index = numbers.index(minimum)
maximum_index = numbers.index(maximum)

numbers.insert(minimum_index, maximum)
numbers.pop(minimum_index + 1)

numbers.insert(maximum_index, minimum)
numbers.pop(maximum_index + 1)

print(*numbers)

# l = [int(i) for i in input().split()]
# x = l.index(min(l))
# y = l.index(max(l))
# l[x], l[y] = max(l), min(l)
# print(*l)