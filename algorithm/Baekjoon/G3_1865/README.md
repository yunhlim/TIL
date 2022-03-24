# [Baekjoon] 1865. 웜홀 [G3]

## 📚 문제

https://www.acmicpc.net/problem/1865

---

## 📖 풀이 - 플로이드 와샬

도로와 가중치가 존재한다. 웜홀은 시간이 거꾸로 가니 음수이다.

가중치가 음수이고 시작위치가 모든 정점이면서, 정점의 개수가 적으니 **플로이드 와샬 알고리즘**을 쓴다!!

## 📒 코드

```python
import sys
input = sys.stdin.readline


for tc in range(int(input().rstrip())):
    n, m, w = map(int, input().split())     # n : 지점의 수 m : 도로의 수 w : 웜홀의 수
    INF = n * 10000
    arr = [[INF] * (n + 1) for _ in range(n + 1)]
    for i in range(m):  # 도로는 방향이 없는 그래프
        s, e, t = map(int, input().split())
        arr[s][e] = min(t, arr[s][e])       # 가장 작은 값을 넣어준다.
        arr[e][s] = min(t, arr[e][s])       # 가장 작은 값을 넣어준다.
    for i in range(w):  # 웜홀은 방향 있는 그래프
        s, e, t = map(int, input().split())
        arr[s][e] = min(-t, arr[s][e])      # 음수도 가장 작은 값을 넣어준다.
    
    for k in range(1, n + 1):       # 거쳐갈 경유지
        for i in range(1, n + 1):   # 출발지
            if k == i:              # 경유지와 출발지는 달라야 한다
                continue
            for j in range(1, n + 1):   # 목적지
                if k == j:          # 경유지와 목적지도 달라야 한다
                    continue
                arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])   # 경유하는 거리가 짧으면 바꿔준다.
    
    for i in range(1, n + 1):
        if arr[i][i] < 0:           # 하나라도 0보다 작으면 YES를 출력
            print('YES')
            break
    else:
        print('NO')
```

## 🔍 결과

![image-20220324231145577](README.assets/image-20220324231145577.png)

플로이드 와샬 알고리즘으로 풀리긴하는데 시간이 오래걸린다.

---

## 📖 풀이 - 벨만 포드(정석적인 풀이)

출발 위치로 돌아오는 건 벨만 포드 알고리즘을 사용한다고 한다..

