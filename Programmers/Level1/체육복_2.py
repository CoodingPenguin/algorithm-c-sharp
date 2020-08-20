def solution(n, lost, reserve):
    reserved = 0
    _lost = sorted(list(set(lost) - set(reserve)))
    _reserve = list(set(reserve) - set(lost))

    for i in _reserve:
        if i-1 in _lost:
            _lost.remove(i-1)
        elif i+1 in _lost:
            _lost.remove(i+1)

    return n-len(_lost)
