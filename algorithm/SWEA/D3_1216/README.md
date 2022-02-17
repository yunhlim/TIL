# [SWEA] 1216. [S/W 문제해결 기본] 3일차 - 회문2 [D3]

## 📚 문제

https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14Rq5aABUCFAYi&categoryId=AV14Rq5aABUCFAYi&categoryType=CODE&problemTitle=1216&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1

---

전에 풀었던 SWEA - 회문을 응용한다.

저번엔 column의 회문을 구할 때 for문으로 확인하여 구했는데 이번엔 전치행렬을 사용한다.

먼저 전치행렬을 구해 새로운 2차원 배열에 담아준다.

col과 row를 동시에 탐색하는데 회문의 길이는 가장 큰 값부터 1까지 순차적으로 탐색한다.

다 찾으면 더 이상 찾을 필요가 없으니 종료시키기 위해 함수에 담고 return 시켜준다.

## 📒 코드

```python
for _ in range(10):
    tc = int(input())
    arr = [input() for _ in range(100)]     # 입력받은 2차원 배열

    arr_t = [[0]*100 for _ in range(100)]   # 2차원 배열을 전치
    for i in range(100):
        for j in range(100):
            arr_t[i][j] = arr[j][i]

    def pallindrome():
        for m in range(100,0,-1):   # m은 회문의 길이
            # row의 회문 탐색
            for i in range(100):
                for j in range(100-m+1):
                    if arr[i][j:j+m] == arr[i][j:j+m][::-1]:
                        print(f'#{tc} {m}')
                        return
                    elif arr_t[i][j:j + m] == arr_t[i][j:j + m][::-1]:
                        print(f'#{tc} {m}')
                        return

    pallindrome()
```

## 🔍 결과 : Pass

