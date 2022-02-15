T = int(input())
for tc in range(1, 1 + T):
    N = int(input())  # 배열의 길이
    arr = list(map(int, input().split()))
    for i in range(10):  # 10개만 정렬
        min_max = i
        if i % 2:  # i가 홀수일 때 최솟값
            for j in range(i, N):
                if arr[min_max] > arr[j]:
                    min_max = j
        else:  # i가 짝수일 때 최댓값
            for j in range(i, N):
                if arr[min_max] < arr[j]:
                    min_max = j
        arr[i], arr[min_max] = arr[min_max], arr[i]  # 최댓값과 교환
    print(f'#{tc} ', end='')
    print(*arr[:10])  # 앞 정렬된 10개만 출력