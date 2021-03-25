n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

p = int(input())
q = int(input())

s = 0
i = 1
for e in a:
    if p <= i and q >= i:
        s += e
    i += 1

print(s)
