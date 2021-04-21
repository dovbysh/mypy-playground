# bits, ones = [5, 3]
# bits, ones = [3, 2]
yyyy = [int(s) for s in input().split()]
bits, ones = yyyy[0], yyyy[1]
maxZeros = bits - ones
maxI = (1 << bits) + 1
for i in range((1 << ones) - 1, (((1 << ones) - 1) << maxZeros) + 1):
    c = i
    points = 0
    zeros = 0
    s = bits
    needNext = False
    while s > 0 and not needNext:
        z = c & 1
        if z == 1:
            points += 1
        else:
            zeros += 1

        if points > ones:
            needNext = True
        if zeros > maxZeros:
            needNext = True

        c = c >> 1
        s -= 1

    if not needNext:
        p = ""
        c = i
        s = bits
        while s > 0:
            z = c & 1
            if z == 1:
                p = "X" + p
            else:
                p = "O" + p

            c = c >> 1
            s -= 1

        print(p)
