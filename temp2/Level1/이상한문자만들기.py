def solution(s):
    result = ""
    count = 0
    for letter in s:
        if letter != " ":
            if count % 2:
                result += letter.lower()
            else:
                result += letter.upper()
            count += 1
            continue
        result += letter
        count = 0
    return result
