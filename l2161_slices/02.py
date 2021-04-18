uname = input()
ok = True
for i in range(0, len(uname)):
    if uname[i] not in "1234567890qwertyuioplkjhgfdsazxcvbnm_":
        print("Неверный символ:", uname[i])
        ok = False
        break

if ok:
    print("OK")
