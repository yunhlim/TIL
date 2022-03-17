# [SWEA] 5177. [파이썬 S/W 문제해결 기본] 8일차 - 이진 힙 [D2]

## 📚 문제

https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDN86AAXw5UW6&subjectId=AWOVJ-_6qfsDFAWg#

---

**이진 최소힙**은 **heapq** 자료구조를 사용할 수 있다. 그렇지만 직접 heapq를 구현해본다.

heapq의 `heappush()`를 구현한다.

입력 받은 값을 맨 마지막에 넣어 준다.

그리고 그 숫자를 조상노드의 값과 비교해서 조상노드가 더 크면 바꾸어 준다.

완전 이진 트리를 구현할 때는 `// 2` 연산을 활용하는 것이 포인트이다.

## 📒 코드

```python
def enq(num):   # 최소 힙에 값 넣기
    global last
    last += 1       # 최소 힙에 들어간 값의 개수를 세준다.
    min_heap[last] = num    # 맨 마지막에 값을 넣어준다.
    c = last
    p = c // 2
    while p > 0 and min_heap[p] > min_heap[c]:  # 조상이 더 크면 바꾼다.
        min_heap[p], min_heap[c] = min_heap[c], min_heap[p]
        c = p
        p = c // 2


t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    last = 0
    min_heap = [0] * (n + 1)    # 최소 힙 배열
    for num in arr:             # 최소 힙에 입력을 다 넣어준다.
        enq(num)
    
    # 조상 노드의 합 구하기
    anc = last // 2             # 조상 노드
    total = 0                   # 조상 노드의 합
    while anc:
        total += min_heap[anc]  # 조상 노드의 값 더하기
        anc //= 2               # 더 상위의 조상 노드로
    print(f'#{tc} {total}')
```

## 🔍 결과 : Pass