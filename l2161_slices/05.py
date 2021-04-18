n = int(input())
for i in range(0, n):
    s = input()
    if s[:3].lower() == "не ":
        print(s[3:])
    else:
        print(s)
