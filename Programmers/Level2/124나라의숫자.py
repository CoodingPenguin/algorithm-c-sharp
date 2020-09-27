def dec_to_124(n):
    lang = '124'
    q, r = divmod(n-1, 3)
    if q == 0:
        return lang[r]
    return dec_to_124(q) + lang[r]

def solution(n):
    return dec_to_124(n)