print(" ".join(str(p) for p in (j * j for j in [int(i) for i in input().split()] if j % 2 == 1) if (p - 9) % 10 != 0))

print(" ".join([str(i ** 2) for i in map(int, input().split()) if i % 2 == 1 and i ** 2 % 10 != 9]))
