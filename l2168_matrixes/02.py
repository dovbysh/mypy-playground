rows = int(input())
cols = int(input())
table = [[input() for _ in range(0, cols)] for _ in range(0, rows)]

for r in range(0, rows):
    print("\t".join(table[r]))
