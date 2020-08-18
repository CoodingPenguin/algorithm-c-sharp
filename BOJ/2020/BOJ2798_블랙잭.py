def blackjack(n, m, cards):
      maxNum = 0
  for i in range(n-2):
    for j in range(i+1, n-1):
      for k in range(j+1, n):
        sumOfCards = cards[i] + cards[j] + cards[k]
        if sumOfCards > maxNum and sumOfCards <= m:
          if sumOfCards == m:
            return m
          maxNum = sumOfCards
  return maxNum

N, M = map(int, input().split())
cards = list(map(int, input().split()))
print(blackjack(N, M, cards))