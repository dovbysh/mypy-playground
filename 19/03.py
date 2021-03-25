n = int(input())
text = []
for i in range(n):
    text.append(input())

i = int(input())

for s in text:
    if i <= len(s):
        print(s[i - 1], sep="", end="")
