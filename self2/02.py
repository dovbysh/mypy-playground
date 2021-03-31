while 1:
    s = input()
    last = s[len(s) - 1]
    if (not last.isalpha()) and (not last.isdigit()):
        break
    if "цирк" in s:
        break
    if len(s) % 7 == 0:
        print(s.upper())
    elif len(s) % 2 == 1:
        print(s.lower())
    else:
        w = s.split(" ")
        r = []
        for z in w:
            r.append(z.capitalize())
        print(" ".join(r))
