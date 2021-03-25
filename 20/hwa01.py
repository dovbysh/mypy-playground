k = int(input())

li = [0, 1, 0, 3, 0, 3, 0]

if k > len(li):
    while k > len(li):
        n = len(li)
        e = 0
        for i in range(n):
            if li[i] == li[n - i - 1]:
                e += 1
        li.append(e)
else:
    li = li[:k]

for e in li:
    print(e)
