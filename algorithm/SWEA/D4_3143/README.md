# [SWEA] 3143. 가장 빠른 문자열 타이핑 [D4]

## 📚 문제

https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV_65wkqsb4DFAWS&categoryId=AV_65wkqsb4DFAWS&categoryType=CODE&problemTitle=3143&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1

---

문자열을 슬라이싱으로 패턴 문자열과 확인하면서 일치하면 전체를 움직이는 것이 포인트이다.

## 📒 코드

```python
T = int(input())
for tc in range(1, T + 1):
    A, B = input().split()  # 문자열 A, 포함된 문자열 B
    s = 0   # 이동하는 인덱스
    cnt = 0 # 중복된 문자열 개수 확인

    while s < len(A)-len(B)+1:  # 검색할 문자열을 넘어가면 종료
        if A[s:s+len(B)] == B:  # 패턴이 존재하는지 확인
            cnt += 1
            s += len(B)         # 존재하면 패턴의 길이만큼 이동
        else:
            s += 1
    print(f'#{tc} {len(A)-cnt*(len(B)-1)}')

```

## 🔍결과 : Pass