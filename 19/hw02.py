n = int(input())
text = []
prices = []
for i in range(n):
    text.append(input())
    prices.append(int(input()))

for i in range(len(text) - 1, -1, -1):
    print(text[i], prices[i])
