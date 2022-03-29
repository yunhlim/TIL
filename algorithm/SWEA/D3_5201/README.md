# [SWEA] 5201. [파이썬 S/W 문제해결 구현] 3일차 - 컨테이너 운반 [D3]

## 📚 문제

https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDYSqAAbw5UW6&subjectId=AWUYEGw61n8DFAVT

---

## 📖 풀이

컨테이너와 트럭을 내림차순으로 정렬한다.

트럭이 큰 순서로 확인한다. 컨테이너도 큰 순서로 확인하며 담을 수 있으면 무게에 더해준다.

컨테이너는 다음 컨테이너부터 확인할 수 있게 시작점 처리를 해준다.

## 📒 코드

```python
for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())    # n:컨테이너의 개수 m:
    containers = list(map(int, input().split()))
    trucks = list(map(int, input().split()))
    containers.sort(reverse=True)
    trucks.sort(reverse=True)
    total = 0       # 총 무게

    s = 0
    for i in range(m):
        for j in range(s, n):
            if trucks[i] >= containers[j]:  # 담을 수 있는 경우
                total += containers[j]      # 무게를 더한다
                s = j + 1                   # 다음 컨테이너 시작점을 지정
                break

    print(f'#{tc} {total}')
```

## 🔍 결과

![image-20220329143349094](README.assets/image-20220329143349094.png)