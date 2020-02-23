W = input()
alpha = [0]*26
for w in W:
    alpha[ord(w)-ord('a')] += 1
for a in alpha:
    print(a, end=" ")
