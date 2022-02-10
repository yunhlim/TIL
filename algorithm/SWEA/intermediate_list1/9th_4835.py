T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())    # N: 정수의 개수, M: 구간의 개수
    num_lst = list(map(int, input().split()))   # 정수 리스트
    num_sum = 0
    for i in range(M):  # 처음 M개의 합을 구한다
        num_sum += i
    min_sum = num_sum   # 합의 최소, 처음 M개의 합으로 초기화
    max_sum = num_sum   # 합의 최대, 처음 M개의 합으로 초기화

    for i in range(1, N-M+1):   # N개 안에서 M개의 배열을 이동시킬 수 있는 경우의 수

        # 이전 M개의 합에서 오른쪽 하나를 더하고 왼쪽 하나를 뺀다.
        num_sum = num_sum - num_lst[i-1] + num_lst[i+M-1]

        if num_sum < min_sum:
            min_sum = num_sum
        elif num_sum > max_sum:
            max_sum = num_sum

    print(f'#{tc} {max_sum - min_sum}')