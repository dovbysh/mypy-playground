s = input()
i1 = -1
i2 = -1
for i in range(0, len(s)):
    if s[i] in "ESM":
        i1 = i
        break

if i1 > -1:
    for i in range(i1 + 1, len(s)):
        if s[i] in "ESM":
            i2 = i
            break

print(i1 + 1)
if i2 == -1:
    i2 = len(s)
if i1 > -1:
    print(i2 - i1 - 1)
else:
    print(i2)

x = set(["E", "S", "M", " "])
ss = (set(s)).difference(x)

print(len(ss))
