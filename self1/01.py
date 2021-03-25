# П у т н и к м е ж д у м и р а м и и в одо ро сл и
t = int(input())
pi = 0
for i in range(t):
    z = i
    if t - z - (2 * z) - (6 * z) < 0:
        print(t - pi - (2 * pi) - 6 * pi, 6 * pi, 2 * pi, pi)
        break
    else:
        pi = z
