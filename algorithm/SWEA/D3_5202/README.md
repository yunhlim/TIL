# [SWEA] 5202. [파이썬 S/W 문제해결 구현] 3일차 - 화물 도크 [D3]

## 📚 문제

https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDYSqAAbw5UW6&subjectId=AWUYEGw61n8DFAVT

---

## 📖 풀이

작업 종료 시간으로 정렬한다.

종료 시간 순으로 넣을 수 있는지 확인하여 넣을 수 있으면 작업 개수를 늘려준다.

순서대로 찾아주기만 하면 끝이다!

## 📒 코드

```python
for tc in range(1, 1 + int(input())):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    arr.sort(key=lambda x: x[1])    # 종료시간으로 정렬
    cnt, end = 0, 0
    for i in range(n):  # 종료시간 낮은 것부터 확인
        s, e = arr[i]
        if end <= s:  # 시작시간이 이전 종료시간보다 크거나 같으면 + 1
            end = e   # 종료시간을 업데이트
            cnt += 1
    print(f'#{tc} {cnt}')
```

## 🔍 결과

![image-20220329143803432](README.assets/image-20220329143803432.png)