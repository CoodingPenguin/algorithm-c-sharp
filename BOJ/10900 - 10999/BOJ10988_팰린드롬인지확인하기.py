def is_palindrome(word):
    length = len(word)
    for i in range(0, length//2):
        if word[i] == word[length - i - 1]:
            continue
        else:
            return 0
    return 1


word = input()
print(is_palindrome(word))
