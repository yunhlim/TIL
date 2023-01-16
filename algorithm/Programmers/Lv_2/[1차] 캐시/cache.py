cacheSize = 1
cities = ["Jeju", "Jeju", "Seoul", "NewYork", "LA"]


def solution(cacheSize, cities):
    class Node:
        def __init__(self, node, prv=None, nxt=None):
            self.node = node
            self.prv = prv
            self.nxt = nxt

    # 대문자로 변경
    for i in range(len(cities)):
        cities[i] = cities[i].upper()
    # 캐시의 크기가 0인 경우
    if cacheSize == 0:
        return len(cities) * 5

    cache = {}
    time = 0
    start = None
    end = None

    for city in cities:

        if not cache.get(city):     # 캐시에 없는 수가 나오는 경우
            time += 5
            cache[city] = Node(city, nxt=start)
            if start:
                cache[start].prv = city
            else:
                end = city

            if cacheSize < len(cache):
                new_end = cache[end].prv
                cache[new_end].nxt = None
                del(cache[end])
                end = new_end

        # 캐시에 있던 경우
        else:
            time += 1
            if start == city:
                continue
            prv = cache[city].prv
            nxt = cache[city].nxt
            if prv:
                cache[prv].nxt = nxt
            if nxt:
                cache[nxt].prv = prv
            if end == city:     # 끝에 있던 경우
                end = prv
            cache[city].prv = None
            cache[city].nxt = start
            cache[start].prv = city
        start = city

    return time


print(solution(cacheSize, cities))
