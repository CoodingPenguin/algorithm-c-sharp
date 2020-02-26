for w in input():
    if w.isdigit() or w.isspace():
        print(w, end='')
        continue
    if w.isupper():
        print(chr(ord('A')+(ord(w)-ord('A')+13) % 26), end='')
    elif w.islower():
        print(chr(ord('a')+(ord(w)-ord('a')+13) % 26), end='')
