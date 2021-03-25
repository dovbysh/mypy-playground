n = int(input())
li = []
for zzz in range(n):
    li.append(int(input()))

p = int(input())
r = False
for i in range(len(li)):
    for j in range(len(li)):
        if i == j:
            continue
        if li[i] * li[j] == p:
            r = True
            break
    if r:
        break

if r:
    print("ДА")
else:
    print("НЕТ")
