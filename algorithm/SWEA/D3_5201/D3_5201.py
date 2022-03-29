for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    containers = list(map(int, input().split()))
    trucks = list(map(int, input().split()))
    containers.sort(reverse=True)
    trucks.sort(reverse=True)
    c, t = 0, 0     # 컨테이너와 트럭을 큰 것부터 확인
    total = 0       # 총 무게

    while t < m and c < n:  # 컨테이너나 트럭이 인덱스를 초과하면 종료
        if trucks[t] >= containers[c]:  # 담을 수 있는 경우
            total += containers[c]
            t += 1                      # 다음 트럭을 담는다.
        c += 1                          # 컨테이너는 항상 다음으로

    print(f'#{tc} {total}')