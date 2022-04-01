# [SWEA] 5208. [파이썬 S/W 문제해결 구현] 5일차 - 전기버스2 [D3]

## 📚 문제

https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDYSqAAbw5UW6&subjectId=AWUYGf7K180DFAVT#

---

## 📖 풀이

처음에 생각했던 건 충전지에서 충전을 하면 그만큼 더 갈 수 있는지 알았다. 그런데 보니까 배터리를 교체해서 이전에 가지고 있는 충전량은 초기화하고 새로 배터리를 가지고 출발하는 것이었다.

따라서 현 위치에서 갈 수 있는 위치를 재귀로 호출하고, 각각 위치에서 충전하여 출발하도록 한다.

가지치기를 통해 반복 횟수를 줄여야 한다. 지속적으로 끝까지 도달하면 교환 횟수를 초기화 하는데 현재 구하고 있는 교환 횟수가 지금까지 구한 최소 교환 횟수보다 크거나 같으면 종료하고 다음 재귀함수를 탐색한다.

## 📒 코드

```python
def recur(cur, change):
    global min_change
    if min_change <= change:        # 가지치기, 교환 횟수가 더 많아지면 X
        return
    if cur >= n:
        min_change = min(min_change, change)
        return
    for i in range(1, arr[cur] + 1):    # 움직일 수 있는 정류장
        recur(cur + i, change + 1)


t = int(input())
for tc in range(1, t + 1):
    arr = list(map(int, input().split()))
    n = arr.pop(0) - 1
    min_change = n
    recur(0, -1)    # 첫 정류장에서 연료를 넣고 출발하는 경우를 빼준다.
    print(f'#{tc} {min_change}')
```

## 🔍 결과

![image-20220401102521757](README.assets/image-20220401102521757.png)