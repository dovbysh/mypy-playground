n = int(input())
text = []
for i in range(n):
    text.append(input())

k = int(input())

for z in range(k):
    i = int(input())
    if i <= len(text):
        print(text[i - 1])
