word = input()
alpha = [-1]*26
for idx, w in enumerate(word):
    diff = ord(w) - ord('a')
    if alpha[diff] == -1:
        alpha[diff] = idx
for a in alpha:
    print(a, end=" ")
