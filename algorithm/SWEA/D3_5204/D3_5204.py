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