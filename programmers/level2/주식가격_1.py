def solution(prices):
    result = []
    for i in range(len(prices)-1):
        count = 0
        for j in range(i+1, len(prices)):
            count += 1
            if prices[i] > prices[j]:
                break
        result.append(count)
    result.append(0)
    return result