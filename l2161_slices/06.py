maxL = int(input())
n = int(input())
for i in range(0, n):
    s = input()
    if len(s) > maxL:
        print(s[:maxL - 3] + "...")
    else:
        print(s)
