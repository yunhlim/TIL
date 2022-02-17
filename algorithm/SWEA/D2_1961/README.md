# [SWEA] 1961. 숫자 배열 회전 [D2]

## 📚 문제

https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5Pq-OKAVYDFAUq&categoryId=AV5Pq-OKAVYDFAUq&categoryType=CODE&problemTitle=1961&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1

---

행렬을 90도 180도 270도를 회전시켜 출력하는 문제이다.

90도 회전하는 함수를 만들어 함수를 한 번 사용하면 90도 두 번 사용하면 180도 세 번 사용하면 270도 회전한 행렬을 구할 수 있다.

각각의 행렬을 하나의 배열에 담아 각 열들을 순차적을 출력시킨다.

## 📒 코드

```python
def rotate(lst):    # 90도 회전하는 함수
    lst_r = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            lst_r[i][j] = lst[N - 1 - j][i]
    return lst_r


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr_r = [0, 0, 0]   # 각각의 배열을 담을 배열 선언
    arr_r[0] = rotate(arr)  # 90도 회전
    arr_r[1] = rotate(arr_r[0]) # 90 + 90 = 180도 회전
    arr_r[2] = rotate(arr_r[1]) # 180 + 90 = 270도 회전
    print(f'#{tc}')

    for i in range(N):
        for j in range(3):  # 각각의 배열의 열들을 순서대로 출력한다.
            print(''.join(map(str, arr_r[j][i])), end=' ')
        print()

```

## 🔍 결과 : Pass