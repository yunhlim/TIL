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

