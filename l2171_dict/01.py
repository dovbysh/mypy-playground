birthMonthes = {}

n = int(input())
for _ in range(n):
    s = input().split(" ")
    if s[2] not in birthMonthes:
        birthMonthes[s[2]] = []
    birthMonthes[s[2]].append(s[0])

n = int(input())
for _ in range(n):
    s = input()
    if s in birthMonthes:
        birthMonthes[s].sort()
        print(" ".join(birthMonthes[s]))
    else:
        print()
