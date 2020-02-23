def result(word):
    rt = ""
    for c in word:
        if c.isupper():
            rt += c.lower()
        else:
            rt += c.upper()
    return rt


print(result(input()))
