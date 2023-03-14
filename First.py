numbers = [8, 9, 10, 11]

numbers.pop(1)
numbers.insert(1, 17)
for i in range(4, 7):
    numbers.append(i)
numbers.pop(0)
numbers += numbers
numbers.insert(3, 25)
print(numbers)

# еще одно решение
# numbers = [8, 9, 10, 11]
# numbers[1] = 17
# numbers.extend([4, 5, 6])
# del numbers[0]
# numbers *= 2
# numbers.insert(3, 25)
# print(numbers)