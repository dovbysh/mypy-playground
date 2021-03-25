s = input()

if len(s) <= 13 and "беззар" <= s and "хлябь" >= s and (("стан" in s and len(s) % 2 == 1) or ("стан" not in s)) and (
        "мир" not in s):
    print("МОЖЕТ")
else:
    print("НЕ МОЖЕТ")
