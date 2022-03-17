# [SWEA] 1486. 장훈이의 높은 선반 [D4]

## 📚 문제

https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV2b7Yf6ABcBBASw&categoryId=AV2b7Yf6ABcBBASw&categoryType=CODE&problemTitle=1486&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1

---

사람을 한 명씩 고르거나 안 고르거나 선택할 수 있다. 따라서 조합이다.

가지치기를 하여 시간복잡도를 줄여준다.

먼저 재귀를 활용해 확인한 cur, 키의 합을 함수의 인자로 사용한다.

> ex). 5명이면 cur이 0부터 1명씩 확인하여 4까지 확인한 후 5에서 종료한다.

고르면 키의 합에 더해주고, 고르지 않으면 cur만 1 늘려준다.

cur이 5인 순간 모든 인원을 확인한 순간이다. 이 때 키의 합이 탑의 높이보다 크거나 같은지 확인한다.

크거나 같으면 result에 담아준다. result는 탑의 높이보다 크거나 같은 수 중 가장 작은 수이다.

따라서 구하는 중간에 result보다 키의 합이 크면 바로 종료시킨다.

## 📒 코드

```python
def recur(cur, total):  # 조합
    global result

    if result <= total:     # result보다 현재 합이 더 크면 종료
        return
    if cur == n:            # 모든 인원을 확인했으면
        if total >= top:    # top보다 크거나 같은지 확인
            result = min(result, total)     # result보다 작은지 확인
        return

    recur(cur + 1, total)   # 현재 사람을 고르는 경우
    recur(cur + 1, total + arr[cur])    # 고르지 않는 경우


t = int(input())
for tc in range(1, t+1):
    n, top = map(int, input().split())
    arr = list(map(int, input().split()))
    result = 10000 * n      # 키가 최대 10000
    recur(0, 0)             # 조합으로 확인
    print(f'#{tc} {result - top}')     # 차이를 출력
```

## 🔍 결과

![image-20220317210053457](README.assets/image-20220317210053457.png)