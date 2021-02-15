zeros, ones = [1, 0], [0, 1]
for i in range(2, 41):
  zeros.append(zeros[i-2]+zeros[i-1])
  ones.append(ones[i-2]+ones[i-1])


for _ in range(int(input())):
  n = int(input())
  print(zeros[n], ones[n])