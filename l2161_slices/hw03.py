n = int(input())
for i in range(0, n):
    s = input()
    if s[:4] != "####":
        if s[:2] == "%%":
            print(s[2:])
        else:
            print(s)
