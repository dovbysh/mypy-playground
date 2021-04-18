rows = int(input())
cols = int(input())
t = [[input() for _ in range(0, cols)] for _ in range(0, rows)]

for r in range(0, rows):
    print("\t".join(t[r]))
print()

for c in range(0, cols):
    for r in range(0, rows):
        print(t[r][c] + "\t", end="")
    print()
