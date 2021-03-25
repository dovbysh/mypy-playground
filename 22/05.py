n = int((input())[1:])
for _ in range(n):
    s = input()
    p = s.find("#")
    if p > -1:
        print((s[:p]).rstrip())
    else:
        print(s.rstrip())
