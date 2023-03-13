n = int(input())
l = []
l2 = []
for _ in range(n):
    s = input()
    l.append(s)
k = int(input())
print(l)
for i in range(len(l)):
    l2.extend(l[i])
    if k <= len(l2):
        print(l2[k-1], end ='')
    del l2[:]

