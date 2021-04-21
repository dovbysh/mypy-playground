s = input()
z = {}
for i in range(0, len(s)):
    c = s[i].lower()
    z[c] = z.setdefault(c, 0) + 1

print(max(z.values()))
