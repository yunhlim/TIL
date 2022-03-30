# [SWEA] 5204. [파이썬 S/W 문제해결 구현] 4일차 - 병합 정렬 [D3]

## 📚 문제

https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDYSqAAbw5UW6&subjectId=AWUYFsQq11kDFAVT#

---

**병합 정렬**을 구현하는 문제이다.

**분할정복**을 활용해 둘로 쪼개나가면서 재귀를 돈다.

재귀의 기저조건으로 배열의 크기가 1이되면 중단한다.

1이 되면 그 때부터 정렬시키며 올라오는 탑다운 방식이다.

쪼갠 걸 합칠 때 정렬시켜야 하는데 두 배열의 왼쪽 값부터 확인하며 더 작은 값을 넣어준다.

넣어주기 위해 인덱스로 파악했는데, 인덱스를 둘다 0으로 출발하고 값을 넣어주면 인덱스를 1씩 더해주었다.

한쪽 배열을 다 담아 인덱스가 배열의 크기보다 커지면, 다른 배열을 다 담고 종료한다.

## 📒 코드

```python
def merge_sort(arr):    # 분할정복 활용 병합 정렬
    global cnt
    if len(arr) == 1:   # 길이가 1일 때 배열을 리턴
        return arr
    mid = (len(arr)) // 2       # 길이가 1보다 크면 둘로 나눈다.
    left = merge_sort(arr[0:mid])   # 왼쪽 정렬 후 left에 담는다.
    right = merge_sort(arr[mid:])   # 오른쪽 정렬 후 right에 담는다.
    if left[-1] > right[-1]:        # 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 큰 경우 cnt +1
        cnt += 1
    l, r = 0, 0     # 왼쪽과 오른쪽 인덱스 표시
    result = []
    while l < len(left) or r < len(right):  # l과 r 둘 다 인덱스를 넘어가면 종료
        if l == len(left):                  # l만 인덱스를 넘은 경우
            result.append(right[r])         # right에서 꺼내 담는다.
            r += 1
        elif r == len(right):               # r만 인덱스를 넘은 경우
            result.append(left[l])          # left에서 꺼내 담는다.
            l += 1
        elif left[l] > right[r]:            # l이 r보다 크면 left에서 꺼내 담는다.
            result.append(right[r])
            r += 1
        elif left[l] <= right[r]:           # r이 l보다 크거나 같으면 right에서 꺼내 담는다.
            result.append(left[l])
            l += 1
    return result

t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    x = merge_sort(arr)[n // 2]
    print(f'#{tc}', x, cnt)
```

## 🔍 결과

![image-20220330173444506](README.assets/image-20220330173444506.png)