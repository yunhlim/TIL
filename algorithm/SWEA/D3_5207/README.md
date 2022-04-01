# [SWEA] 5207. [파이썬 S/W 문제해결 구현] 4일차 - 이진 탐색 [D3]

## 📚 문제

https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do

---

## 📖 풀이

이진탐색 문제이다. 문제에 함정이 많이 숨겨져있다.

먼저 우리가 입력을 정렬시켜야 한다. sort()로 정렬을 시킨다.

그리고 이진탐색을 하는데 한쪽 방향으로 두 번 들어가는 순간 탐색을 종료시켜야 한다.

따라서 check 변수를 만들어 한 쪽 방향으로 두 번 들어가는 순간 종료시키도록 코드를 짠다.

## 📒 코드

```python
def binary_search(x):
    s, e = 0, n - 1
    check = 0
    while s <= e:
        mid = (s + e) // 2
        if a[mid] == x:
            return True
        elif a[mid] > x:
            if check == 1:
                break
            check = 1
            e = mid - 1
        else:
            if check == 2:
                break
            check = 2
            s = mid + 1
    return False


for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    total = 0
    for num in b:
        total += binary_search(num)
    print(f'#{tc} {total}')
```

## 🔍 결과

![image-20220401101358902](README.assets/image-20220401101358902.png)

문제 이해를 못해서 한참 헤맸다😢😢