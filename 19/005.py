n = int(input())
text = []
for i in range(n):
    text.append(input())

k = int(input())
search = []
for i in range(k):
    search.append(input())

for s in text:
    matched = True
    for ss in search:
        if s.find(ss) == -1:
            matched = False
            break
    if matched:
        print(s)
