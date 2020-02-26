W = input().upper()
alphas = [0]*26
for w in W:
    alphas[ord(w) - ord('A')] += 1
countSorted = sorted(alphas)
if countSorted[-1] == countSorted[-2]:
    print("?")
else:
    print(f"{chr(alphas.index(countSorted[-1])+ord('A'))}")