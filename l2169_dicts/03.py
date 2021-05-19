s = input().split(" ")
d = {}
for w in s:
    if w == "":
        continue
    if w in d:
        d[w] += 1
    else:
        d[w] = 1
    print(d[w], end=" ")
