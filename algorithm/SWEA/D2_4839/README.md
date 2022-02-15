# [SWEA] 4839. [파이썬 S/W 문제해결 기본] 2일차 - 이진탐색 [D2]

## 📚 문제

https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do

---

이진 탐색을 해보는 문제이다. 풀면서 느낀건데 수가 가운데에 존재하지 않으면 엄청 오랫동안 탐색해야한다는 단점이 있다.

A, B 두 학생이 이진 탐색을 해야하므로, 이진 탐색을 하는 함수를 따로 만들어주었다.

## 📒 코드

```python
def search_cnt(pages, page):  # 이진 탐색하는 횟수를 출력
    cnt = 1
    start = 1
    end = pages
    while page != (start + end) // 2:  # page를 찾으면 탐색 종료
        cnt += 1
        if page > (start + end) // 2:
            start = (start + end) // 2
        else:
            end = (start + end) // 2
    return cnt


T = int(input())
for tc in range(1, T + 1):
    P, A, B = map(int, input().split())  # P: 전체 쪽수 A, B: A, B가 찾을 쪽 번호
    cnt_A = search_cnt(P, A)  # A가 찾을 횟수
    cnt_B = search_cnt(P, B)  # B가 찾을 횟수
    win = 0
    if cnt_A == cnt_B:  # 비기면 0
        win = 0
    elif cnt_A > cnt_B:  # 횟수가 더 적은 쪽이 이긴다.
        win = 'B'
    else:
        win = 'A'
    print(f'#{tc} {win}')
```

## 🔍 결과 : Pass