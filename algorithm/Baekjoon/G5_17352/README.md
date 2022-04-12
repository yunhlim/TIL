# [Baekjoon] 17352. 여러분의 다리가 되어 드리겠습니다! [G5]

## 📚 문제

https://www.acmicpc.net/problem/17352

---

## 📖 풀이

끊어진 걸 연결해야하기 때문에 연결요소가 아닌 유니온 파인드가 좀 더 명확하다. 두 가지의 연결요소를 BFS, DFS로도 찾을 수 있지만, **유니온 파인드**로 해결해본다.

유니온 파인드의 **경로압축**과 **union-by-rank**를 활용해 find 과정과 unoin 과정에서 최적화 해준다. 특히 union-by-rank를 하지 않는 경우 재귀 깊이 에러가 발생해서 추가해주었다.

n-2개를 다 연결시켜준 후, set 자료형으로 n개를 find하여 담아준다.

그러면 2개만 남는 데 그걸 출력한다.

## 📒 코드

```python
def find(x):
    if par[x] != x:
        par[x] = find(par[x])   # 경로 압축
    return par[x]


def union(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return
    if rnk[a] < rnk[b]:         # union-by-rank
        par[a] = b
    elif rnk[a] > rnk[b]:
        par[b] = a
    else:
        rnk[b] += 1
        par[a] = b


n = int(input())
par = [i for i in range(n + 1)]
rnk = [0 for _ in range(n + 1)]
for i in range(n - 2):
    a, b = map(int, input().split())
    union(a, b)

result = set()
for i in range(1, n + 1):
    result.add(find(i))
    if len(result) == 2:
        break
print(*result)
```

## 🔍 결과

![image-20220412105958493](README.assets/image-20220412105958493.png)