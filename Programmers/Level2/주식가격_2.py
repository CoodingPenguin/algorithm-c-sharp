from collections import deque


def solution(prices):
    result = []
    prices = deque(prices)

    while prices:
        # 가장 앞의 요소 가져오기
        target = prices.popleft()
        count = 0
        # 그 이후의 가격과 일일이 비교 및 카운트
        # 바로 떨어져도 1초를 고려하므로 떨어져도 +1
        for price in prices:
            if target > price:
                count += 1
                break
            count += 1
        result.append(count)

    return result
