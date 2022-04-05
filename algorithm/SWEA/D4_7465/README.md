# [SWEA] 7465. 창용 마을 무리의 개수 [D4]

## 📚 문제

https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWngfZVa9XwDFAQU&categoryId=AWngfZVa9XwDFAQU&categoryType=CODE&problemTitle=7465&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1

---

**연결 요소** 문제이다. **Union - Find 알고리즘**을 활용해 풀어본다.

find()로 root를 찾는 함수를 만들고, 이 때 경로 압축 과정을 포함시켜 root 바로 밑으로 경로들을 줄여준다.

입력으로 연결시킬 두 정점을 꺼내 두 정점의 root 값이 다르면 union() 함수로 병합해준다.

두 정점의 root 값이 같으면 어차피 연결되어 있으므로 다음 입력을 확인한다.

이렇게 다 union()으로 다 연결시켜준 후, 모든 정점들의 root 값을 찾아서 set() 자료형에 담는다. 중복된 값은 사라지니 중복되지 않는 root들만 남게 된다.

이 root를 출력하면 그 때가 연결 요소의 개수이다.

## 📒 코드

```python
def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x]) # 경로 압축
    return parent[x]


def union(a, b):
    p_a = find(a)
    p_b = find(b)
    if p_a < p_b:           # 수가 작은 것으로 root를 합쳐나간다.
        parent[p_b] = parent[p_a]
    else:
        parent[p_a] = parent[p_b]


t = int(input())
for tc in range(1, t + 1):
    n, m = map(int, input().split())

    parent = [i for i in range(n + 1)]      # 각 정점들을 자신의 값으로 root를 초기화한다.
    for i in range(m):
        v1, v2 = map(int, input().split())  # 입력으로 받은 연결된 두 정점
        if find(v1) == find(v2):    # root가 같으면 continue
            continue
        union(v1, v2)       # root가 다르면 합쳐준다.

    root = set()
    for i in range(1, n + 1):   # root의 총 개수를 찾는다.(연결 요소의 개수)
        root.add(find(i))

    print(f'#{tc} {len(root)}')
```

## 🔍 결과

![image-20220405162414013](README.assets/image-20220405162414013.png)