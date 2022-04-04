# [SWEA] 1251. [S/W 문제해결 응용] 4일차 - 하나로 [D4]

## 📚 문제

https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15StKqAQkCFAYD&categoryId=AV15StKqAQkCFAYD&categoryType=CODE&problemTitle=%ED%95%98%EB%82%98%EB%A1%9C&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1

---

## 📖 풀이

사이클 없이 연결해야 하고, 가중치가 가장 적게 연결시키는 경우를 찾는 문제이므로 **최소신장트리**를 만드는 문제이다. 여기서는 **크루스칼 알고리즘**을 적용해본다.

간선이 많으므로 사실 크루스칼 알고리즘보다 프림 알고리즘이 좋다.

일단 둘 다 처음이므로 크루스칼 알고리즘으로 우선 풀어본다.

크루스칼 알고리즘은 최소신장트리를 만들어주는 알고리즘 중 하나이다.

모든 경로가 트리로 연결되어야 한다. 즉, cycle이 없어야 한다.

cycle을 없애는 방법으로 Union-FInd 알고리즘을 활용한다.

**Union-Find 알고리즘**을 활용해 루트를 찾고, 루트를 기준으로 병합해주어야 한다.

> Union-Find란?
>
> 트리를 이용해 합집합을 만들어가는 과정이다.
>
> Union 함수와 Find 함수를 만들어서 사용한다.
>
> 모든 정점마다 root를 담아주는 리스트를 선언한다. 처음에 모든 정점의 root는 자기 자신으로 초기화한다.
>
> Find 함수는 정점의 root를 찾아주는 함수이다.
>
> 이 때, root를 찾을 때 경로 압축(Path Compression)을 해주어야 속도를 개선할 수 있다. 루트를 찾아가는 과정에 있는 모든 것들의 root를 root로 변경해준다.
>
> Union 함수는 두 정점의 root가 다를 때 root를 합쳐준다. root의 크기가 큰 것을 작은 것에 합친다.(root를 정점이 작은 것으로 합쳐나가는 방법으로 생각한다.)

간선들을 연결해보는 순서는 가중치로 정렬해 가중치가 작은 순서로 정렬한다. 왜냐면 최소신장트리를 만들어야 하기 때문이다.

정점이 n개이면 트리의 모든 정점을 연결하는 경우는 n-1개의 간선이 연결될 때이니 이 때 stop한다.

## 📒 코드

```python
def find(x):            # root 찾기
    if root[x] != x:
        root[x] = find(root[x])     # 경로 압축 : 부모가 중간에 바꼈을 때 전부다 root로 직접 연결시켜준다.
    return root[x]


def union(a, b):       # 병합
    r_a = find(a)       # a의 root
    r_b = find(b)       # b의 root
    if r_a < r_b:       # 큰 root를 더 작은 root로 바꾼다.
        root[r_b] = r_a
    else:
        root[r_a] = r_b


t = int(input())
for tc in range(1, 1 + t):
    n = int(input())
    arr_x = list(map(int, input().split()))
    arr_y = list(map(int, input().split()))
    e = float(input())
    edges = []

    for i in range(n):
        x1, y1 = arr_x[i], arr_y[i]
        for j in range(i + 1, n):
            x2, y2 = arr_x[j], arr_y[j]
            edges.append([(x1 - x2) ** 2 + (y1 - y2) ** 2, i, j])    # 거리와 노드들을 리스트에 담는다.
    edges.sort()    # 거리로 정렬
    root = [i for i in range(n)]
    cnt = 0         # 연결된 간선의 개수
    result = 0      # 출력할 거리 제곱의 합

    for i in range(len(edges)):
        if cnt == n - 1:            # 트리를 모두 연결한 경우
            break
        d, n1, n2 = edges[i]
        if find(n1) != find(n2):    # root가 다른 경우
            union(n1, n2)           # 합쳐준다.
            cnt += 1                # 연결한 간선의 개수를 +1
            result += d
    
    print(f'#{tc} {int(result * e + 0.5)}')     # 마지막에 e를 곱한다. 반올림이니 0.5를 더하고 정수형변환
```

## 🔍 결과

![image-20220404230548815](README.assets/image-20220404230548815.png)
