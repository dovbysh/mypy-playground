menu = ["щи", "борщ", "щавелевый суп", "овсяный суп", "суп по-чабански"]
days = int(input())
i = 0
for z in range(days):
    print(menu[i])
    i += 1
    if i >= len(menu):
        i = 0
