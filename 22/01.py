a = [int(i) for i in input().split()]
m, k = (int(i) for i in input().split())
print(sum(a[m:k + 1]))
