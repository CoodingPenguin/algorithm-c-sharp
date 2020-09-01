def solution(s, n):
    result = ''
    for letter in s:
        if letter != ' ':
            if letter.isupper():
                letter = chr(ord('A') + (ord(letter)+n-ord('A'))%26)
            else:
                letter = chr(ord('a') + (ord(letter)+n-ord('a'))%26)
        result += letter
    return result