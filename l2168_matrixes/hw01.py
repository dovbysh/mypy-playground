n = int(input())
h = []
v = ["" for _ in range(0, n)]
for _ in range(0, n):
    s = input()
    h.append(s)
    for i in range(0, n):
        v[i] = v[i] + s[i]

found = False
for i in range(0, n):
    if "xxx" in h[i] or "xxx" in v[i]:
        print("x")
        found = True
        break
    elif "ooo" in h[i] or "ooo" in v[i]:
        print("o")
        found = True
        break

if not found:
    print("-")
