s = input()
o = 0
for i in range(0, len(s)):
    if s[i] == "о":
        if o == 0:
            o = 1
        j = i + 1
        while j < len(s) and s[j] == "о":
            if j - i + 1 > o:
                o = j - i + 1
            j += 1

print(o)
