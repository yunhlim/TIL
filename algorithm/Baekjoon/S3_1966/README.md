# [Baekjoon] 1966. 프린터 큐 [S3]

## 📚 문제 : [프린터 큐](https://www.acmicpc.net/problem/1966)

## 📖 풀이

큐를 활용한 문제이다. 우리는 처음 주어진 수들의 인덱스를 알고있어야 하고, 큐의 움직임에 따라 처음 인덱스를 놓치지 않아야 하니 (중요도, 처음 인덱스)로 값을 담아 배열에 2차원으로 넣어줘야 한다.

따라서 zip 함수를 활용해 중요도와 처음 인덱스로 이루어진 1차원 배열을 묶는다.

이 때 중요도로 내림차순 정렬을 시켜 하나 씩 꺼낼 때마다, 최댓값이 무엇인지 확인할 것이다.

따라서 중요도로 이루어진 배열을 내림차순 정렬시켜야 하는데, 그러면 zip 함수도 따라 바뀌게 된다. 그러므로 새로운 변수를 선언해 거기에 중요도로 이루어진 배열을 정렬시킨 후 담아준다.

중요도가 제일 높은 경우 큐의 뒤로 보내지않고 버리기만 한다. 이 때 버린 개수를 세고, 버리는 수의 처음 인덱스 값이 원하는 값과 같으면 그 때의 버린 개수를 출력한다.

중요도가 제일 높지 않은 경우는 큐의 맨 뒤로 보낸다.

## 📒 코드

```python
from collections import deque


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    temp = list(map(int, input().split()))
    idx_arr = [i for i in range(n)]
    zip_arr = zip(temp, idx_arr)
    rnk_arr = sorted(temp, reverse=True)
    que = deque(zip_arr)
    cnt = 0

    while que:
        rnk, idx = que.popleft()
        if rnk_arr[cnt] == rnk:
            cnt += 1
            if idx == m:
                print(cnt)
                break
            continue
        else:
            que.append((rnk, idx))
```

## 🔍 결과

![image-20220729000501759](README.assets/image-20220729000501759.png)