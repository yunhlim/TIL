# [SWEA] 1234. [S/W 문제해결 기본] 10일차 - 비밀번호 [D3]

## 📚 문제

https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14_DEKAJcCFAYD&categoryId=AV14_DEKAJcCFAYD&categoryType=CODE&problemTitle=%EB%B9%84%EB%B0%80%EB%B2%88%ED%98%B8&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1

---

그 전에 풀었던 반복문자 지우기와 매우 유사하다. 해설은 반복문자 지우기 게시글을 참고!

## 📒 코드

```python
# 비밀번호
for tc in range(1, 11):
    N, arr = input().split()
    arr = list(arr)
    s = 0
    while s < len(arr): # 이전 값과 비교하여 없애고 없애면 하나 전 인덱스로 이동해 다시 확인
        if s and arr[s] == arr[s-1]:    # s가 0이 아닐 때 이전 값과 비교
            del arr[s], arr[s-1]    # 같을 땐 값을 지우고 이전 인덱스로 이동해 비교한다.
            s -= 1
        else:   # 다를 땐 다음 인덱스로 이동한다.
            s += 1
    print(f'#{tc} {"".join(arr)}')
```

## 🔍 결과 : Pass