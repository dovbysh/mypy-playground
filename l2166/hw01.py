c = input().lower()
s = input().split()
for i in range(0, len(s)):
    if c in s[i].lower():
        print(s[i])
