w = input().split(", ")
s = input()
res = []
for z in w:
    if z.upper() == z:
        res.append(z)

if len(res) > 0:
    print(s.join(res))
