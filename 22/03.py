n = int(input())
for i in range(n):
    p = input().find("кот")
    if p > -1:
        print(i + 1, p + 1)
