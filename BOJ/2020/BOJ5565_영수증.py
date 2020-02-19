total = int(input())
prices = []

for i in range(9):
    prices.append(int(input()))

print(total - sum(prices))
