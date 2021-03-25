n = int(input())
text = []
for i in range(n):
    text.append(input())

search = input()

for s in text:
    if s.find(search) > -1:
        print(s)
