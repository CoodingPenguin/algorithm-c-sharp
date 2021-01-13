from collections import deque


def solution(cacheSize, cities):
    if not cacheSize:
        return len(cities) * 5
    cache = deque()
    result = 0
    for city in cities:
        city = city.lower()
        # 캐시 히트
        if city in cache:
            result += 1
            cache.remove(city)
            cache.append(city)
        else:
        # 캐시 미스
            result += 5
            if len(cache) < cacheSize:
                cache.append(city)
            else:
                cache.popleft()
                cache.append(city)
    return result