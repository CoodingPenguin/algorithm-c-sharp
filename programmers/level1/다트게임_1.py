def solution(dartResult):
    result = []
    for i, symbol in enumerate(dartResult):
        try:
            n = int(symbol)
            if result and n == 0 and result[-1] == 1:
                result.pop()
                n = 10
            result.append(n)
        except:
            if symbol == 'D':
                n = result.pop()
                result.append(n**2)
            elif symbol == 'T':
                n = result.pop()
                result.append(n**3)
            elif symbol == '*':
                result[-1] *= 2
                try:
                    result[-2] *= 2
                except:
                    pass
            elif symbol == '#':
                n = result.pop()
                result.append(-n)
    return sum(result)
