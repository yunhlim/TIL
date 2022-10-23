# [Programmers] Lv 2. [1차] 캐시 [2018 KAKAO BLIND RECRUITMENT]

## 📚 문제 : [[1차] 캐시](https://school.programmers.co.kr/learn/courses/30/lessons/17680)

## 📖 풀이

**LRU** 알고리즘을 알면 쉽고 모르면 생각을 해야할 문제이다.

순수 알고리즘 지식 이외의 CS 지식도 요구한다. 그렇지만 몰라도 조금만 이해해보면 논리를 이해하고 풀 수 있다.

도시 이름을 확인할 때, 캐시에 없다면 캐시에 추가하면서 도시 이름을 가져온다. 이 때 실행 시간은 5이다.

캐시에 있다면, 캐시에 있는 도시 이름을 가져온다. 그리고 가장 최근에 사용한 캐시로 위치를 이동시킨다. 실행 시간은 1이다.

캐시가 가득찼는데 새로운 도시를 캐시에 넣으면, 가장 오래 있던(나중에 사용했던) 캐시가 없어진다. 이는 큐를 활용해 계산하면 된다.

**deque를 활용해도 remove 함수를 사용할 수 있다.**

캐시의 길이가 30까지로 짧으니 그냥 리스트로 선언하여 해결했다.

## 📒 코드

```python
def solution(cacheSize, cities):
    cache = []
    time = 0
    for city in cities:
        new_city = ""
        for c in city:
            if 'a' <= c <= 'z':
                new_city += chr(ord(c) - 32)
            else:
                new_city += c
        city = new_city

        if city in cache:
            cache.remove(city)
            time += 1
        else:
            time += 5
            if len(cache) == cacheSize:
                cache.pop(0)
        cache.append(city)
    return time
```

## 📖 링크드리스트 풀이

링크드리스트를 구현하여 풀어본다.

파이썬에 deque을 사용할 수 있지만, search에서 O(n)이 걸린다. 

따라서 링크드 리스트를 Class로 새로 만들어 준다. 그리고 **딕셔너리**를 활용한다.

- 딕셔너리를 활용해 cache에 해당 city가 있을 때 O(1)로 조회할 수 있다.

### city가 캐시에 없는 경우

- city를 맨 앞에 작성해주고 원래 맨 앞에 있던 도시와 연결한다.
- 캐시가 가득 찬 경우에는 맨 뒤에 있는 city를 없앤다.

### city가 캐시에 있는 경우

- city를 맨 앞으로 이동한다.
- 원래 맨 앞에 있던 경우는 수정하지 않는다.
- 끝에 있던 경우는 끝을 가리키는 포인터를 한 칸 당겨야 한다.

캐시의 크기가 0인 경우는 그냥 cities의 길이에 5를 곱해 출력하면 된다.

## 📒 링크드리스트 + 해시맵 코드

```python
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
```

