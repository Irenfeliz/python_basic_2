#encryption and decryption
phrase = input()
new_phrase = ''
encryption = input('Would you like encryption or decryption? e/d ').strip()
lang = input('Would you like to use rus or eng language? r/e ').strip()
step = int(input('Please specify the step of encryption: '))

if lang == 'r':
    amount_of_characters = 32
    begin_uppers = 1040
    begin_lowers = 1072
    end_uppers = 1071
    end_lowers = 1103
else:
    amount_of_characters = 26
    begin_uppers = 65
    begin_lowers = 97
    end_uppers = 90
    end_lowers = 122

if encryption == 'e':
    for i in phrase:
        if i.isalpha():
            if i.isupper() and (ord(i) + step) > end_uppers:
                new_phrase += chr(ord(i) + step - amount_of_characters)
            elif i.islower() and (ord(i) + step) > end_lowers:
                new_phrase += chr(ord(i) + step - amount_of_characters)
            else:
                new_phrase += chr(ord(i) + step)
        else:
            new_phrase += chr(ord(i))
else:
    for i in phrase:
        if i.isalpha():
            if i.isupper() and (ord(i) - step) < begin_uppers:
                new_phrase += chr(ord(i) - step + amount_of_characters)
            elif i.islower() and (ord(i) - step) < begin_lowers:
                new_phrase += chr(ord(i) - step + amount_of_characters)
            else:
                new_phrase += chr(ord(i) - step)
        else:
            new_phrase += chr(ord(i))

print(new_phrase)