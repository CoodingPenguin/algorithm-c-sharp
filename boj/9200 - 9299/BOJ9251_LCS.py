seq1, seq2 = input(), input()
l1, l2 = len(seq1), len(seq2)
table = [[0]*(l2+1) for _ in range(l1+1)]

for i in range(1, l1+1):
  for j in range(1, l2+1):
    if seq1[i-1] == seq2[j-1]:
      table[i][j] = table[i-1][j-1] + 1
    else:
      table[i][j] = max(table[i-1][j], table[i][j-1])

print(table[l1][l2])