# s = input()
# s = s.lower()
# text = s.split()
# print('Общее количество артиклей:', text.count('a') + text.count('an') + text.count('the'))

start = input()
l = start.replace('#', '')
n = int(l)
text = ''

for _ in range(n):
    t = input()
    text += t + '\n'

textlist = text.split('\n')
for i in range(len(textlist)):
    index = textlist[i].find('#')
    if index > -1:
        print(textlist[i][:index].rstrip())
    else:
        print(textlist[i].rstrip())

# короткое решение:
# n = input()
# for _ in range(int(n[1:])):
#     s = input()
#     if '#' in s:
#         s = s[:s.find('#')]
#     print(s.rstrip())