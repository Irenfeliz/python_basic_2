# На вход программе подается строка текста на английском языке, в которой нужно зашифровать все слова.
# Каждое слово строки следует зашифровать с помощью шифра Цезаря
# (циклического сдвига на длину этого слова).
# Строчные буквы при этом остаются строчными, а прописные – прописными.
# Формат входных данных
# На вход программе подается строка текста на английском языке.
#
# Формат выходных данных
# Программа должна вывести зашифрованный текст в соответствии с условием задачи.
#
# Примечание. Символы, не являющиеся английскими буквами, не изменяются.

def encryption(phrase, step):
    new_phrase = ''
    amount_of_characters = 26
    end_uppers = 90
    end_lowers = 122
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
    return new_phrase

phrase = input()
word_new = ''
result = ''
for word in phrase.split():
    for letter in word:
        if letter.isalpha():
            word_new += letter
    result += encryption(word, len(word_new)) + ' '
    word_new = ''

print(result)