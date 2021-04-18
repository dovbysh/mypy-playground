n = int(input())
for i in range(0, n):
    s = input()
    cat = s.find("кот")
    if cat > -1:
        print(i + 1, cat + 1)
