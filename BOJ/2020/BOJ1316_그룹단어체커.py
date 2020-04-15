def is_group(word):
    alphabet = [False] * 26
    for i in range(len(word)):
        idx = ord(word[i]) - ord('a')
        if not alphabet[idx]:
            alphabet[idx] = True
        else:
            if not (word[i-1] == word[i]):
                return False
    return True


cnt = 0
for _ in range(int(input())):
    if is_group(input()):
        cnt += 1
print(cnt)
