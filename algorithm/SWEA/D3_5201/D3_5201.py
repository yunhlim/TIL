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