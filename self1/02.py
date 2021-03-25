v1 = float(input())
v2 = float(input())
v3 = float(input())
s = float(input())
t = float(input()) / 60
res = []
if v1 * t > s:
    res.append("человек")
if v2 * t > s:
    res.append("геддар")
if v3 * t > s:
    res.append("кханнан")

if len(res) > 0:
    print(" ".join(res))
else:
    print("Не они")
