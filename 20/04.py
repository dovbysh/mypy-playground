n = int(input())
li = []
for zzz in range(n):
    li.append(input())

n = len(li)
for i in range(n - 1):
    for j in range(n - 1 - i):
        if len(li[j]) > len(li[j + 1]):
            li[j], li[j + 1] = li[j + 1], li[j]
        elif len(li[j]) == len(li[j + 1]):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]

for s in li:
    print(s)
