n = int(input())
p = i = 0
for zzz in range(n):
    c = int(input())
    if i > 0:
        print(p + c)
    p = c
    i += 1
