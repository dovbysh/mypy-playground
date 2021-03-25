n = int(input())
li = []
for zzz in range(n):
    li.append(input())

k = int(input())

for zzz in range(k):
    n = int(input())
    newLi = []
    for zzzz in range(n):
        i = int(input())
        newLi.append(li[i - 1])
    li = newLi

for s in li:
    print(s)
