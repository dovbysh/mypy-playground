n = int(input())
# n=5
li = []
for i in range(n + 1):
    if i == 0:
        li.append((i, 1))
    else:
        k = i
        d = k % 2
        for j in range(i):
            if j % 2 == d and j > 0:
                k *= j
        li.append((i, k))

print(li)
