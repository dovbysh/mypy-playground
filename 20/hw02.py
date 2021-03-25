n = int(input())
li = []
for zzz in range(n):
    li.append(int(input()))

n = len(li)
for i in range(n - 1):
    for j in range(n - 1 - i):
        if li[j] < li[j + 1]:
            li[j], li[j + 1] = li[j + 1], li[j]

for s in li:
    print(s)
