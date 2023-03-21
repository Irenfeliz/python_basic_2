import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'

chars = ''

print('How many passwords do you need?')
amount = int(input())

print('How many characters should be in your password?')
length = int(input())

print('Should it include digits? y/n')
include_digits = input()
if include_digits.lower() == 'y':
    chars += digits

print('Should it include uppercase letters? y/n')
include_uppercase_letters = input()
if include_uppercase_letters.lower() == 'y':
    chars += uppercase_letters

print('Should it include lowercase letters? y/n')
include_lowercase_letters = input()
if include_lowercase_letters.lower() == 'y':
    chars += lowercase_letters

print('Should it include punctuation? y/n')
include_punctuation = input()
if include_punctuation.lower() == 'y':
    chars += punctuation


print('Should ambiguous symbols "il1Lo0O" be excluded? y/n')
ambiguous_symbols = input()
if ambiguous_symbols.lower() == 'y':
    for i in chars:
        if i in 'il1Lo0O':
            chars = chars.replace(i, '')

def generate_password(length, chars):
    return ''.join(random.sample(chars, length))


for _ in range(amount):
    password = generate_password(length, chars)
    print(password)
