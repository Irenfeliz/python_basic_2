n = int(input())
l = []
for i in range(n):
    k = int(input())
    l.append(k)
del l[1::2]
print(l)