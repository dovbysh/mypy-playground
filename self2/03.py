for zz in range(int(input())):
    s1 = set(z for z in [int(i) for i in input().split(" ? ")] if z % 2 == 0)
    s2 = set(z for z in [int(i) for i in input().split(" ? ")] if z % 2 == 0)
    rs = [z for z in (s2 - s1)]
    rs.sort()
    print(" * ".join(str(z) for z in rs))
