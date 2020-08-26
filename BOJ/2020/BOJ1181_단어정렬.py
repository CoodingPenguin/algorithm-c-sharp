import sys

words = []
for _ in range(int(sys.stdin.readline())):
  words.append(sys.stdin.readline().strip())

words = sorted(list(set(words)))
words = sorted(words, key=lambda x:len(x))
for word in words:
  print(word)