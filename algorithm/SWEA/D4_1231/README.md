# [SWEA] 1231. [S/W 문제해결 기본] 9일차 - 중위순회 [D4]

## 📚 문제

https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV140YnqAIECFAYD&categoryId=AV140YnqAIECFAYD&categoryType=CODE&problemTitle=1231&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1

---

**완전이진트리**로 값을 넣는다. 따라서 입력에서는 노드의 연결도 알려줬지만 중요하지 않다.

순서대로 값만 리스트에 담아준다.

그리고 이진트리의 중위순회를 사용해서 출력한다.

## 📒 코드

```python
def in_order(v):
    global last
    if v <= last:
        return in_order(v*2) + tree[v] + in_order(v*2+1)    # 완전 이진트리의 중위순회 방법
    else:
        return ''


for tc in range(1, 11):
    n = int(input())
    tree = [0 for _ in range(n + 1)]
    last = 0
    for i in range(1, n + 1):
        tree[i] = input().split()[1]    # 트리에 값을 넣는다. 완전이진트리니 순서대로 넣어 구현
        last += 1
    print(f'#{tc} {in_order(1)}')
```

## 🔍 결과 : Pass