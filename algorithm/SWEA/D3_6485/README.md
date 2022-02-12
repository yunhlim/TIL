# [SWEA] 6485. 삼성시의 버스 노선 [D3]

## 📚 문제

https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWczm7QaACgDFAWn&categoryId=AWczm7QaACgDFAWn&categoryType=CODE&problemTitle=%EC%82%BC%EC%84%B1%EC%8B%9C&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1

---

카운트 배열 활용 문제

문제는 복잡한데 어렵지 않다.

총 정류장이 5000개인데 1부터 세므로 5001개의 리스트를 만들고 앞에 0번째 리스트는 사용하지 않는다.

정류장의 노선이 겹치면 해당하는 범위에 리스트를 1씩 올려준다.

## 📒 코드

```python
T = int(input())

for tc in range(1, T+1):
    N = int(input())  # 버스의 개수
    bus_lst = [0 for _ in range(5000+1)] # 총 정류장 리스트
    for _ in range(N):
        A, B = map(int, input().split()) # 버스의 노선을 담는다.
        for i in range(A, B+1): # 버스가 지나가는 노선에 1씩 추가한다.
            bus_lst[i] += 1
    P = int(input())    # 출력할 정류장의 개수
    result_lst = [0 for _ in range(P)]
    for i in range(P):
        result_lst[i] = bus_lst[int(input())]

    print(f'#{tc} ', end='')
    print(*result_lst)
```

## 🔍 결과: **Pass**