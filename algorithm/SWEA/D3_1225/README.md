# [SWEA] 1225. [S/W 문제해결 기본] 7일차 - 암호생성기 [D3]

## 📚 문제

https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14uWl6AF0CFAYD&categoryId=AV14uWl6AF0CFAYD&categoryType=CODE&problemTitle=1225&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1

---

queue 문제이다.

왼쪽에서 숫자를 꺼내 특정 연산을 한 후 오른쪽에 다시 넣는 걸 반복한다.

연산은 -1, -2, -3, -4, -5, -1, ...을 반복하고 값이 0이하가 되면 0으로 만든 후 오른쪽에 넣고 끝낸다.

deque 자료형을 사용해 만들어 보았다.

1 ~ 5를 반복시켜주기 위해 cnt를 1씩 증가시키고 %5로 나누어 준다.

그러면 0 ~ 4가 반복되니 1을 더해준다.

## 📒 코드

```python
from collections import deque

for _ in range(10):
    tc = int(input())
    queue = deque(map(int, input().split()))

    cnt = 0
    while queue[-1]:    # 큐의 끝이 0이면 종료
        cnt %= 5    # 1, 2, 3, 4, 5 로 나누게 설정
        cnt += 1
        
        right = queue.popleft() - cnt   # 왼쪽에서 꺼낸 후 연산한다.
        if right > 0:                   # 오른쪽에 넣어준다.
            queue.append(right)
        else:                           # 0보다 작거나 같으면 0을 넣어준다.
            queue.append(0)
    
    print(f'#{tc}', *queue)
```

## 🔍 결과 : Pass