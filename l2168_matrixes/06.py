r = int(input())

t = [input().split(",") for _ in range(0, r)]

n = int(input())
for _ in range(0, n):
    xy = [int(e) for e in input().split(",")]
    print(t[xy[0]][xy[1]])
