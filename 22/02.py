a = [int(i) for i in input().split()]
m, k = (int(i) for i in input().split())
print(sum((i ** 2 for i in a[m:k + 1])))
