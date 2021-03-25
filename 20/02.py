n = int(input())
li = []
for zzz in range(n):
    s = input()
    print(s)
    n, m = s.split("\t")
    if int(m) > 3:
        li.append(s)

print()

for s in li:
    print(s)
