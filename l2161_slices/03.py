s1 = input()
s2 = input()
bull = 0
cow = 0

for i in range(0, len(s1)):
    if s1[i] == s2[i]:
        bull = bull + 1
    else:
        for j in range(0, len(s2)):
            if s1[i] == s2[j]:
                cow += 1

print(bull, cow)
