n = int(input())
li = []
for zzz in range(n):
    li.append(input())

x = int(input())
z = int(input())
i = 1
zz = 0
for p in li:
    if i % x == 0:
        zz = z

    if zz == 0:
        print(p)
    else:
        zz -= 1

    i += 1
