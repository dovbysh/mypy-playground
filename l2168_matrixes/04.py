p = []
for _ in range(0, int(input())):
    c = [1]
    for i in range(0, len(p)):
        el = p[i]
        if i + 1 < len(p):
            el += p[i + 1]
        c.append(el)
    p = c
    print("\t".join([str(e) for e in c]))
