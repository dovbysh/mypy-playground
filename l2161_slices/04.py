n = int(input())

d = "ABCDEFGHIJKLMNOP"
for i in range(n, 0, -1):
    z = []
    for j in range(0, n):
        z.append(d[j] + str(i))
    print(" ".join(z))
