s = [int(input()) for _ in range(0, int(input()))]

subs = set()
for i in range(0, len(s)):
    for j in range(0, len(s)):
        subs.add(s[i] - s[j])

z = list(subs)
z.sort()
for i in range(0, len(z)):
    print(z[i])
