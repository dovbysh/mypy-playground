n = int(input())
li = []
for zzz in range(n):
    s = input()
    found = False
    for i in range(len(li)):
        c, ss = li[i]
        if ss == s:
            li[i] = (c + 1, ss)
            found = True
            break

    if not found:
        li.append((1, s))

for co in li:
    print(co)
