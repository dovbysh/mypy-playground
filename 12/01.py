n = int(input())

for i in range(n):
    for j in range(n):
        print((j + 1) * (i + 1), end="\t")
    print()
